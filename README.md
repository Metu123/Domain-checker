Domain Checker — Domain & URL Availability Tool

Domain Checker is a fast, modern, and lightweight web tool that lets you instantly verify whether a domain or URL is live, reachable, and properly configured using public DNS and RDAP APIs.

It runs entirely in the browser — no backend required.

---

Features

- Instant domain checking
- Supports:
  - Bare domains ("example.com")
  - Subdomains ("api.example.com")
  - Full URLs ("https://example.com")
- DNS Resolution:
  - A records (IP addresses)
  - CNAME records
- RDAP Lookup:
  - Registration date
  - Expiry date
  - Registrar info
- Detailed Results UI
- Smart status detection:
  - Active
  - Registered (no DNS)
  - Not found (NXDOMAIN)
- Local history (last 8 checks)
- Clean, modern UI with animations

---

How It Works

Domain Checker combines:

1. DNS-over-HTTPS (DoH)

Queries:

- https://dns.google/resolve
- https://cloudflare-dns.com/dns-query

Used to determine:

- If domain resolves
- IP addresses
- CNAME chains

---

2. RDAP (Registration Data Access Protocol)

Queries:

- https://rdap.org
- Verisign fallback

Used to fetch:

- Registration date
- Expiration date
- Registrar
- Domain status

---

Status Logic

Condition| Result
A record exists| Active
CNAME exists| Active (via CNAME)
No records but DNS OK| Registered (no config)
NXDOMAIN| Not found
DNS failure| Uncertain

---

Setup

Option 1: Run locally (recommended)

Due to browser CORS restrictions, open via a local server.

Using VS Code:

1. Install Live Server
2. Right-click "index.html"
3. Click "Open with Live Server"

Using Python:

python -m http.server 8000

Then open:

http://localhost:8000

---

Option 2: Open directly (not recommended)

Opening the HTML file directly may cause:

- DNS requests to fail
- CORS errors

---

Project Structure

domain-checker/
│
├── index.html   # Full app (HTML + CSS + JS)
└── README.md    # Documentation

---

Privacy

- No backend
- No data stored remotely
- All checks happen in-browser
- History stored only in "localStorage"

---

Limitations

- Some networks may block DNS-over-HTTPS
- RDAP data depends on registry availability
- No HTTP status check (only DNS-level validation)
- CORS policies may affect behavior

---

Future Improvements

- HTTP status check (200, 404, etc.)
- Server geolocation
- Response time tracking
- SSL certificate validation
- WHOIS fallback
- Bulk domain checker
- Backend API option

---

Author

Nwuzor Christian

---

License

MIT License — free to use, modify, and distribute.
