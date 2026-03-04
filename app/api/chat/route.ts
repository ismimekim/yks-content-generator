import { NextRequest, NextResponse } from "next/server";
import { buildSystemPrompt } from "@/lib/prompts";
import { detectIntent, getPromptMode } from "@/lib/intent-detector";
import type { Message, Platform, Language, StyleSource } from "@/lib/types";

interface ChatRequestBody {
  messages: Message[];
  platform: Platform;
  contentType: string;
  language: Language;
  styleSource?: StyleSource;
  trends?: string[];
}

export async function POST(req: NextRequest) {
  try {
    const body: ChatRequestBody = await req.json();
    const { messages, platform, contentType, language, styleSource, trends } = body;

    // Validate request
    if (!messages || !Array.isArray(messages)) {
      return NextResponse.json(
        { error: "Messages array is required" },
        { status: 400 }
      );
    }

    const apiKey = process.env.OPENROUTER_API_KEY || "";
    const baseURL = "https://openrouter.ai/api";

    if (!apiKey) {
      return NextResponse.json(
        { error: "OPENROUTER_API_KEY not configured" },
        { status: 500 }
      );
    }

    const lastUserMessage =
      [...messages].reverse().find((m) => m.role === "user")?.content ?? "";
    
    // Detect user intent to determine appropriate mode
    const detectedIntent = detectIntent(lastUserMessage);
    const mode = getPromptMode(detectedIntent.intent);

    // Build system prompt
    const systemPrompt = buildSystemPrompt({
      platform,
      contentType,
      language,
      styleSource: styleSource ?? "oguz_usta",
      mode,
      lastUserMessage,
      trends,
    });

    // Convert messages to OpenRouter/OpenAI format (system message first)
    // Note: systemPrompt may contain Turkish chars, but that's handled by fetch
    const openRouterMessages = [
      { role: "system" as const, content: systemPrompt },
      ...messages.map((msg) => ({
        role: msg.role as "user" | "assistant",
        content: msg.content,
      })),
    ];

    // Debug: log the request size to catch overly large prompts
    const requestBodyObj = {
      model: "anthropic/claude-sonnet-4-6",
      max_tokens: 4096,
      messages: openRouterMessages,
      stream: true,
    };
    
    console.log("Request body size:", JSON.stringify(requestBodyObj).length, "chars");

    // Call OpenRouter API
    const response = await fetch(`${baseURL}/v1/chat/completions`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": `Bearer ${apiKey}`,
        "HTTP-Referer": "http://localhost:3002",
        "X-Title": "Odaklan SM - YKS Content Creator",
      },
      body: JSON.stringify(requestBodyObj),
    });

    if (!response.ok) {
      const error = await response.text();
      console.error("OpenRouter API error:", response.status, error);
      return NextResponse.json(
        { error: `API error: ${response.status}` },
        { status: response.status }
      );
    }

    // Stream the response
    const encoder = new TextEncoder();
    const decoder = new TextDecoder();
    
    const readableStream = new ReadableStream({
      async start(controller) {
        try {
          const reader = response.body?.getReader();
          if (!reader) {
            throw new Error("No response body");
          }

          let sseBuffer = "";
          const processBuffer = (flush = false) => {
            const events = sseBuffer.split("\n\n");
            if (!flush) {
              sseBuffer = events.pop() ?? "";
            } else {
              sseBuffer = "";
            }

            for (const event of events) {
              const dataLines = event
                .split("\n")
                .filter((line) => line.startsWith("data: "))
                .map((line) => line.slice(6).trim());

              for (const data of dataLines) {
                if (!data || data === "[DONE]") {
                  continue;
                }

                try {
                  const parsed = JSON.parse(data);

                  // OpenRouter/OpenAI format: choices[0].delta.content
                  if (parsed.choices?.[0]?.delta?.content) {
                    const text = parsed.choices[0].delta.content;
                    controller.enqueue(
                      encoder.encode(`data: ${JSON.stringify({ text })}\n\n`)
                    );
                  }
                  // Anthropic format fallback: content_block_delta
                  else if (
                    parsed.type === "content_block_delta" &&
                    parsed.delta?.type === "text_delta"
                  ) {
                    const text = parsed.delta.text;
                    controller.enqueue(
                      encoder.encode(`data: ${JSON.stringify({ text })}\n\n`)
                    );
                  }
                } catch {
                  // Ignore parse errors on non-JSON lines.
                }
              }
            }
          };

          while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            sseBuffer += decoder.decode(value, { stream: true });
            processBuffer(false);
          }

          sseBuffer += decoder.decode();
          processBuffer(true);

          controller.enqueue(encoder.encode("data: [DONE]\n\n"));
          controller.close();
        } catch (error) {
          console.error("Streaming error:", error);
          controller.error(error);
        }
      },
    });

    return new NextResponse(readableStream, {
      headers: {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        Connection: "keep-alive",
      },
    });
  } catch (error) {
    console.error("Chat API error:", error);
    return NextResponse.json(
      { error: "Failed to process chat request" },
      { status: 500 }
    );
  }
}
