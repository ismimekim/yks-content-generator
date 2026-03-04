import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  // API rotaları ve statik dosyaları atla
  if (
    request.nextUrl.pathname.startsWith('/api/') ||
    request.nextUrl.pathname.startsWith('/_next/') ||
    request.nextUrl.pathname.startsWith('/favicon') ||
    request.nextUrl.pathname === '/password'
  ) {
    return NextResponse.next()
  }

  // Cookie'den auth kontrolü
  const authCookie = request.cookies.get('yks-auth')
  
  if (authCookie?.value === 'true') {
    return NextResponse.next()
  }

  // Auth yoksa password sayfasına yönlendir
  return NextResponse.redirect(new URL('/password', request.url))
}

export const config = {
  matcher: [
    /*
     * Match all request paths except:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico, sitemap.xml, robots.txt (metadata files)
     */
    '/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
  ],
}
