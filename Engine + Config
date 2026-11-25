// DIDACTIC-ENGINE — server.js
// Port: 14831 (Rare Prime Port)
// Run: npm install express && node server.js

const express = require('express');
const app = express();

const PORT = process.env.DIDACTIC_ENGINE_PORT || process.env.PORT || 14831;
const HOST = process.env.HOST || '0.0.0.0';

app.use(express.json());

// Health check
app.get('/', (req, res) => {
  res.json({
    engine: 'DIDACTIC-ENGINE',
    status: 'alive',
    port: PORT,
    throne: 'active',
    dragon: 'guarding',
    secret_type: '[a-z] + numeric prime vault',
    timestamp: new Date().toISOString()
  });
});

// Vault check — never expose real secret, only validation shape
app.get('/vault/status', (req, res) => {
  const hasSecret = Boolean(process.env.DIDACTIC_SECRET);
  const hasNumeric = Boolean(process.env.DIDACTIC_NUMERIC_KEY);
  res.json({
    secret_configured: hasSecret,
    numeric_key_configured: hasNumeric,
    port: PORT
  });
});

// CodeQL-safe example endpoint
app.post('/engine/echo', (req, res) => {
  const { input } = req.body || {};
  if (typeof input !== 'string' || input.length > 1000) {
    return res.status(400).json({ error: 'Invalid input — must be string <= 1000 chars' });
  }
  res.json({ echo: input, engine: 'DIDACTIC-ENGINE' });
});

app.listen(PORT, HOST, () => {
  console.log(`🐉 DIDACTIC-ENGINE listening on http://${HOST}:${PORT}`);
  console.log(`   Throne: active | Dragon: guarding | Port: ${PORT}`);
});
