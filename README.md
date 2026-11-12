# Avyra Company website

Static, bilingual (Arabic default at `/`, English at `/en/`) site for Avyra Company / شركة أفيرا. Pages: home, about, services, projects (experience), team, contact, privacy.
Built from the Alkarar Arrow site template (same fonts, CSS and JS).

## Editing
All content and settings live in `build.py`. Edit, then run `python3 build.py` and commit the regenerated HTML.

Settings to fill in at the top of `build.py`: `SITE` (domain), `EMAIL`, `PRIVACY_EMAIL`, `PHONE_*`, `LINKEDIN_URL`,
`BOOKING_URL`, `CR`, and the contact form endpoint (`FORM_ENDPOINT` / `FORM_KEY`, Web3Forms or Formspree).
Empty values hide the matching row or button.

## Hosting
Any static host (Cloudflare Pages, Netlify). Root-relative paths: serve from a domain root. `_headers` holds security headers.
