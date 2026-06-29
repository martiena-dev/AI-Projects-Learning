# AI Engineering Transition — Progress Tracker

> **How to use this file:** This is the source of truth for my 6-month plan. I keep it in my
> repo and update it as I finish things. When I start a NEW chat with Claude, I paste this whole
> file into my first message so Claude knows exactly where I am and what's next.
> (Claude does not remember past chats, so this file is how I carry context forward.)

---

## About Me (context for any new session)

- **Name:** Martiena (single name, no surname)
- **Current role:** Python backend developer at Elmeasure, working on the Theiox IoT platform
- **Stack I know:** Python, FastAPI, MongoDB, MQTT, MCP (Model Context Protocol) servers, React, Three.js
- **Background:** Aeronautical engineering -> Python trainee -> backend developer (3+ years)
- **Goal:** Transition into AI engineering and land a senior role (India / remote / abroad) in ~6 months
- **My wedge / positioning:** Production MCP servers + FastAPI AI-backend systems
- **Constraints:**
  - Working from an **office laptop** (planning to buy a used ThinkPad by ~Month 2)
  - **Cloud-first** setup — everything runs in the browser (Codespaces, Kaggle, Colab)
  - **Budget-conscious** — free tools/courses preferred; will pay only for small, high-value things
- **Learning style:** Learn by building, step-by-step, beginner-level explanations, ONE step at a time

---

## Accounts & Setup (reference)

- **Dev email:** martiena.codes@gmail.com (or whichever I created)
- **GitHub:** github.com/martiena-dev
- **Blog (live):** martiena-blog.vercel.app
- **Experiments repo:** github.com/martiena-dev/AI-Projects-
- **Password manager:** Bitwarden
- **LLM API in use:** Google Gemini (free tier) — model `gemini-2.5-flash`
- **Other accounts:** Hugging Face, Kaggle, Vercel, OpenRouter, Google AI Studio

---

## Overall Plan (6 Months / 26 Weeks)

| Phase            | Weeks | Focus                                                                       |
|------------------|-------|-----------------------------------------------------------------------------|
| **Foundation**   | 1–8   | Setup, cloud workflow, LLM API basics, RAG + evals foundation, Flagship 1   |
| **Differentiators** | 9–16 | Flagship 1 polish, Flagship 2 (MCP red-team), first fine-tune, first OSS PRs |
| **Convert**      | 17–26 | Resume/portfolio, networking, applications, interviews, offers              |

**Flagship projects planned (all cloud / free-infra friendly):**
1. **MCP Red-Team CLI ("Adversarial Promptbook")** — scans MCP servers for vulnerabilities (my wedge)
2. **Domain-Specific LoRA Fine-Tune** — Indic-language extraction, runs on free Kaggle GPU
3. *(Medium)* **Hybrid Retrieval Service** — FastAPI + pgvector + BM25 + reranker
4. *(Medium)* **Trace Theatre Lite** — Three.js 3D visualization of agent traces

---

## PROGRESS LOG

### [DONE] Week 1 — Setup & First Artifact (COMPLETE)

- [x] Created dev email (martiena.codes@gmail.com)
- [x] Set up Bitwarden password manager + 2FA on Gmail & GitHub
- [x] Created accounts: GitHub, Hugging Face, Kaggle, Vercel, OpenRouter, Google AI Studio
- [x] Installed VS Code + Git; set up work/personal separation (per-folder git config)
- [x] Deployed blog to Vercel (Blog Starter Kit template) -> live at martiena-blog.vercel.app
- [x] Cleaned URL, removed sample posts, added avatar (UI Avatars initial "M")
- [x] **Published first blog post:** "Why I'm Learning AI Engineering in 2026"

### [IN PROGRESS] Week 2 — Cloud Dev + First LLM Call

- [x] **Day 1:** Found & opened GitHub Codespaces; created `AI-Projects-` repo; ran first
      Python in the cloud (`hello.py`)
- [x] **Day 2:** First LLM API call
  - [x] Got Gemini API key, stored in Bitwarden
  - [x] Created `.env` (secret key) + `.gitignore` (protects `.env` and `.venv`)
  - [x] Set up `venv`, installed `google-genai` + `python-dotenv`
  - [x] Wrote & ran `gemini_hello.py` — got a real AI response (model: `gemini-2.5-flash`)
  - [x] Debugged a `429 RESOURCE_EXHAUSTED` rate-limit error (switched models)
  - [x] Learned `.env` vs `venv` deeply
  - [x] Created `requirements.txt` (`pip freeze`)
  - [x] Handled first Git divergent-branches / merge situation
  - [x] **Verified `.env` is git-ignored** (`git check-ignore .env`) — key is secure
  - [x] Learned the `git add` -> `commit` -> `push` workflow
- [ ] **Day 3:** Control the model — prompts, system prompts, multi-turn chat, temperature, tokens
- [ ] **Day 4:** Start Karpathy's "Let's build GPT" (first part) + set up info diet (newsletters, X)
- [ ] **Day 5:** Write blog post #2 ("Setting Up My AI Engineering Journey: Week 1") + reflect

### [NOT STARTED] Weeks 3–4 — RAG & Evals Foundation
- [ ] Build a small rigorous RAG (hybrid search + reranker), measure Recall@10
- [ ] Write a 30-case eval suite, calibrate an LLM-as-judge
- [ ] Blog post on retrieval results

### [NOT STARTED] Weeks 5–8 — Flagship 1 begins
- [ ] (Plan to be detailed when I reach this point)

### [NOT STARTED] Weeks 9–16 — Differentiators
- [ ] Flagship 2: MCP Red-Team CLI
- [ ] First LoRA fine-tune on Kaggle
- [ ] First OSS PRs
- [ ] (Detailed later)

### [NOT STARTED] Weeks 17–26 — Convert
- [ ] Resume rewrite + portfolio site
- [ ] Networking (AI Tinkerers Bengaluru, Latent Space Discord, X)
- [ ] Applications + interview prep
- [ ] (Detailed later)

---

## Key Things I've Learned (my own notes)

- An LLM API call = send a prompt, get text back. That's the core of AI engineering.
- `.env` holds **secrets** (never goes to GitHub); `venv` holds **libraries** (rebuildable,
  never goes to GitHub). Both are listed in `.gitignore`.
- `requirements.txt` is the small file that lets others rebuild `venv`. It DOES go to GitHub.
- Git workflow: `git add <files>` -> `git commit -m "message"` -> `git push`.
- Free Gemini models have different rate limits; `gemini-2.5-flash` worked when `2.0-flash` hit 429.
- Always stop Codespaces when done (`github.com/codespaces` -> Stop) to save free hours.

---

## Resources Shortlist (free, curated)

**Courses (free):** Karpathy "Neural Networks: Zero to Hero" - HuggingFace LLM/Agents/MCP courses -
Anthropic Skilljar MCP - Stanford CS336 - DeepLearning.ai short courses - evals.info

**Books:** Raschka "Build an LLM from Scratch" (free GitHub repo) - Chip Huyen "AI Engineering"
(+ free huyenchip.com blog) - Anthropic "Building Effective Agents" (free essay)

**Newsletters:** Simon Willison (simonwillison.net) - Latent Space - hamel.dev - eugeneyan.com -
Sebastian Raschka "Ahead of AI"

**Communities:** Latent Space Discord - HuggingFace Discord - AI Tinkerers Bengaluru -
AGI House India - r/LocalLLaMA - MCP Discord

**Free cloud stack:** GitHub Codespaces - Kaggle (free GPU) - Google Colab - Modal ($30/mo credits) -
Neon (pgvector) - MongoDB Atlas - Vercel - Render - Hugging Face - Gemini/OpenRouter (free LLM APIs) -
Langfuse (observability)

---

## Next Session — Start Here

**Current position:** Week 2, about to start **Day 3** (controlling the model: prompts,
system prompts, multi-turn chat, temperature, tokens).

**To resume:** Paste this whole file into a new chat and say
"ready for Week 2 Day 3" (or wherever I am).
