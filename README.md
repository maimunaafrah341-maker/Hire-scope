# 🔍 HireScope
> AI-powered hiring risk & blindspot detector built for the **Forge Inspira 2026 Codeathon**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)](https://streamlit.io)
[![LLM](https://img.shields.io/badge/AI-Featherless%20LLM-purple)](https://featherless.ai)

---

## 🧠 What it does

HireScope is an AI hiring agent that analyses candidate profiles and surfaces risks that human recruiters typically miss — bias blindspots, career red flags, inconsistencies — and delivers a structured hire/no-hire decision with reasoning.

**No manual review. No gut feeling. Just data.**

---

## ⚙️ How it works

```
LinkedIn URL → Bright Data scrapes live profile → Featherless AI runs 3-step analysis → Hire/No-Hire decision + risk report
```

**3-Step AI Pipeline:**
1. 📋 **Profile Analysis** — Summarises candidate background
2. ⚠️ **Risk & Blindspot Detection** — Flags gaps, inconsistencies, potential biases
3. ✅ **Hiring Decision** — Scored recommendation (out of 10) with reasoning

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| **Bright Data** | Live LinkedIn profile scraping |
| **Featherless AI** | Open-source LLM reasoning engine |
| **Streamlit** | Interactive web dashboard |
| **Python** | Core agent logic & API orchestration |

---

## 🚀 Run it locally

```bash
git clone https://github.com/maimunaafrah341-maker/Hire-scope
cd Hire-scope
pip install -r requirements.txt
```

Create a `.env` file:
```
BRIGHT_DATA_API_KEY=your_key
FEATHERLESS_API_KEY=your_key
```

```bash
streamlit run app.py
```

---

## 🏆 Built at

**Forge Inspira 2026 Codeathon** — Problem Statement: Hiring Risk & Blindspot Detector
