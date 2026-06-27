# Saurav Kishore — AI Agent Chat Dashboard

A dark-minimal animated AI Agent chat interface that introduces my professional profile — experience, skills, projects, and patents — through sequentially-revealed messages with a monospace "AI Agent composing…" typing indicator.

**[🌐 Live Demo](https://Saurav-Kishore.github.io/personal-web-app/)**

## ✨ Features

- Dark charcoal & amber palette — elegant, minimal, easy on the eyes
- "AI Agent" framing — the chat introduces itself as an AI agent representing Saurav
- Sequential message reveal with animated monospace "AI Agent composing…" typing label
- Slide-up animations on every chat bubble
- Responsive design — looks great on mobile and desktop
- Original design language — not inspired by any existing app
- Self-contained single file — no dependencies, no server

## 🚀 Host on GitHub Pages (Free)

### Step 1 — Push to GitHub

```bash
git remote add origin https://github.com/Saurav-Kishore/personal-web-app.git
git branch -M main
git push -u origin main
```

### Step 2 — Enable Pages

1. Go to your repo on GitHub → **Settings** → **Pages**
2. Under **Source**, select **Deploy from a branch**
3. Branch: `main`, folder: `/ (root)`
4. Click **Save**

Your site will be live at `https://Saurav-Kishore.github.io/personal-web-app/` within ~1 minute.

> **Tip:** `index.html` at the repo root is all GitHub Pages needs. No build step, no framework, no configuration.

## 💻 Local Development

### Option A — Just open the file

```bash
open index.html
```

No server needed. The profile data is embedded, animations play instantly.

### Option B — Python server (for the API)

```bash
source .venv/bin/activate
uvicorn main:app --reload
```

- `/` — serves the dashboard (same as `index.html`)
- `/api/profile` — returns profile data as JSON

## ✏️ Customise

Edit the `PROFILE` object at the top of the `<script>` in `index.html` with your own data. The message builder below it automatically renders whatever fields you provide.

## 📁 Structure

```
.
├── index.html          # Standalone static site (deploy to GitHub Pages)
├── main.py             # FastAPI server (optional, for local dev)
├── requirements.txt    # Python dependencies
└── README.md
```
