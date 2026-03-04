import { NextRequest, NextResponse } from "next/server";

interface SearchRequestBody {
  query: string;
  platform?: string;
}

interface TavilyResult {
  title: string;
  url: string;
  content: string;
  score: number;
}

interface TavilyResponse {
  results: TavilyResult[];
  answer?: string;
}

export async function POST(req: NextRequest) {
  try {
    const body: SearchRequestBody = await req.json();
    const { query, platform } = body;

    if (!query) {
      return NextResponse.json(
        { error: "Query is required" },
        { status: 400 }
      );
    }

    const apiKey = process.env.TAVILY_API_KEY;
    if (!apiKey) {
      return NextResponse.json(
        { error: "Tavily API key not configured" },
        { status: 500 }
      );
    }

    // Build search query
    const currentYear = new Date().getFullYear();
    const searchQuery = platform
      ? `${query} ${platform} trends ${currentYear}`
      : `${query} social media trends ${currentYear}`;

    // Call Tavily API
    const tavilyResponse = await fetch("https://api.tavily.com/search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        api_key: apiKey,
        query: searchQuery,
        search_depth: "advanced",
        max_results: 10,
        include_images: false,
        include_answer: true,
      }),
    });

    if (!tavilyResponse.ok) {
      throw new Error(`Tavily API error: ${tavilyResponse.status}`);
    }

    const data: TavilyResponse = await tavilyResponse.json();

    // Extract and format results
    const results = data.results.map((r: TavilyResult) => ({
      title: r.title,
      url: r.url,
      snippet: r.content?.substring(0, 300) || "",
      score: r.score,
    }));

    // Extract trend keywords from results
    const trends = extractTrends(data.results);

    return NextResponse.json({
      results,
      answer: data.answer,
      trends,
    });
  } catch (error) {
    console.error("Search API error:", error);
    return NextResponse.json(
      { error: "Failed to search" },
      { status: 500 }
    );
  }
}

// Extract trending topics from search results
function extractTrends(results: TavilyResult[]): string[] {
  const trends: string[] = [];
  
  for (const result of results) {
    const content = `${result.title} ${result.content || ""}`;
    
    // Extract potential trend terms
    const trendPatterns = [
      /trending?:?\s*([^.]+)/gi,
      /viral:?\s*([^.]+)/gi,
      /popular:?\s*([^.]+)/gi,
      /#(\w+)/g,
    ];

    for (const pattern of trendPatterns) {
      const matches = content.matchAll(pattern);
      for (const match of matches) {
        const trend = match[1]?.trim();
        if (trend && trend.length > 3 && trend.length < 100 && !trends.includes(trend)) {
          trends.push(trend);
        }
      }
    }
  }

  return trends.slice(0, 10); // Return top 10 trends
}
