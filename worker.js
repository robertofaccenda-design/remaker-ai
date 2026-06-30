/**
 * ReMaker AI — Cloudflare Worker proxy per Gemini API
 *
 * La chiave GEMINI_API_KEY non è nel codice — è un secret Cloudflare.
 * Per impostarla: wrangler secret put GEMINI_API_KEY
 *
 * Endpoint:
 *   POST /analyze   — proxy verso Gemini 2.0 Flash
 */

const GEMINI_URL =
  'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent';

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

export default {
  async fetch(request, env) {

    // ── Preflight CORS ──────────────────────────────────────────────────────
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }

    const url = new URL(request.url);

    // ── Healthcheck ─────────────────────────────────────────────────────────
    if (url.pathname === '/' || url.pathname === '/health') {
      return new Response(JSON.stringify({ status: 'ok' }), {
        headers: { 'Content-Type': 'application/json', ...CORS_HEADERS },
      });
    }

    // ── /debug (temporaneo) ──────────────────────────────────────────────────
    if (url.pathname === '/debug') {
      return new Response(JSON.stringify({
        hasKey: !!env.GEMINI_API_KEY,
        keyLength: env.GEMINI_API_KEY?.length || 0,
        envKeys: Object.keys(env).filter(k => k !== 'ASSETS')
      }), { headers: { 'Content-Type': 'application/json', ...CORS_HEADERS } });
    }

    // ── /analyze ─────────────────────────────────────────────────────────────
    if (url.pathname === '/analyze' && request.method === 'POST') {
      if (!env.GEMINI_API_KEY) {
        return new Response(
          JSON.stringify({ error: { message: 'GEMINI_API_KEY non configurata nel Worker.' } }),
          { status: 500, headers: { 'Content-Type': 'application/json', ...CORS_HEADERS } }
        );
      }

      let body;
      try {
        body = await request.json();
      } catch {
        return new Response(
          JSON.stringify({ error: { message: 'Body JSON non valido.' } }),
          { status: 400, headers: { 'Content-Type': 'application/json', ...CORS_HEADERS } }
        );
      }

      const geminiRes = await fetch(`${GEMINI_URL}?key=${env.GEMINI_API_KEY}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      });

      const data = await geminiRes.json();

      return new Response(JSON.stringify(data), {
        status: geminiRes.status,
        headers: { 'Content-Type': 'application/json', ...CORS_HEADERS },
      });
    }

    // ── File statici (index.html, remaker-test.html, ecc.) ──────────────────
    return env.ASSETS.fetch(request);
  },
};
