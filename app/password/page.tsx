'use client'

import { useState } from 'react'

const CORRECT_PASSWORD = 'yks2026' // Basit şifre

export default function PasswordGate() {
  const [password, setPassword] = useState('')
  const [error, setError] = useState(false)
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    setError(false)

    // Basit şifre kontrolü
    if (password === CORRECT_PASSWORD) {
      // Cookie'yi set et ve redirect
      document.cookie = 'yks-auth=true; path=/; max-age=86400' // 24 saat
      window.location.href = '/'
    } else {
      setError(true)
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 to-slate-800 p-4">
      <div className="max-w-md w-full">
        <div className="bg-slate-800/50 backdrop-blur border border-slate-700 rounded-2xl p-8 shadow-2xl">
          {/* Logo/Header */}
          <div className="text-center mb-8">
            <div className="text-4xl mb-4">🦉</div>
            <h1 className="text-2xl font-bold text-white mb-2">YKS Content Generator</h1>
            <p className="text-slate-400 text-sm">Oğuz Usta Style Social Media Content</p>
          </div>

          {/* Password Form */}
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label htmlFor="password" className="block text-sm font-medium text-slate-300 mb-2">
                Şifre
              </label>
              <input
                id="password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full px-4 py-3 bg-slate-900/50 border border-slate-600 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                placeholder="Şifrenizi girin..."
                autoFocus
                disabled={isLoading}
              />
            </div>

            {error && (
              <div className="bg-red-500/10 border border-red-500/20 rounded-lg p-3">
                <p className="text-red-400 text-sm text-center">❌ Hatalı şifre</p>
              </div>
            )}

            <button
              type="submit"
              disabled={isLoading || !password}
              className="w-full bg-purple-600 hover:bg-purple-700 disabled:bg-slate-700 disabled:text-slate-500 text-white font-medium py-3 px-4 rounded-lg transition-colors"
            >
              {isLoading ? 'Kontrol ediliyor...' : 'Giriş Yap'}
            </button>
          </form>

          {/* Footer */}
          <div className="mt-8 text-center">
            <p className="text-slate-500 text-xs">
              AI-powered content creation for YKS coaches
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
