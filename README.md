# waind.org

Personal site built with Pelican.

## Local development

```bash
# Install dependencies
uv sync

# Serve locally with auto-reload
make serve
```

Site will be available at http://localhost:8000

## Adding content

### New note

Create a file in `content/notes/`:

```markdown
Title: My Note Title
Date: 2025-01-03
Slug: my-note-title

Content goes here.
```

### Edit pages

Pages live in `content/pages/`. Edit `index.md`, `now.md`, etc.

## Deployment

Push to `main` branch. GitHub Actions builds and deploys automatically.

## Domain setup (one-time)

In Namecheap DNS settings:

| Type | Host | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | flockoftravi.github.io |

In GitHub repo settings:
1. Settings → Pages
2. Source: GitHub Actions
3. Custom domain: waind.org
4. Enforce HTTPS: ✓
