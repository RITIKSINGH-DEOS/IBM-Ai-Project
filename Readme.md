# 🎬 AI Content Creator Assistant

An AI-powered content creation tool built using **Python**, **Streamlit**, and **Google Gemini AI**.

This application helps content creators generate YouTube scripts, descriptions, hashtags, and analyze thumbnails using AI.

---

## 🚀 Features

### 🎬 Script Generator

Generate high-retention YouTube scripts based on:

* Video Topic
* Video Duration
* Target Audience
* Language (English / Hinglish)

Includes:

* Catchy Title
* Powerful Hook
* Full Script
* Call To Action (CTA)

---

### 📝 Description Generator

Generate SEO-optimized YouTube descriptions.

Features:

* Creator-style descriptions
* SEO-friendly content
* Keyword suggestions
* Call To Action
* Relevant hashtags

---

### 🏷️ Hashtag Generator

Generate topic-based YouTube hashtags to improve discoverability and reach.

Features:

* Trending hashtags
* Niche hashtags
* SEO-focused hashtag suggestions

---

### 🖼️ Thumbnail Analyzer

Analyze YouTube thumbnails using AI.

Provides:

* Overall Score
* Text Readability
* Color Contrast
* Attention-Grabbing Ability
* CTR Potential
* Strengths & Weaknesses
* Improvement Suggestions

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* Pillow (PIL)
* python-dotenv

---

## 📂 Project Structure

```text
AI Content Creator Assistant/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI-Content-Creator-Assistant
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Get your API key from Google AI Studio.

---

## ▶️ Run The Application

```bash
streamlit run app.py
```

---

## 🌟 Future Improvements

* Title Generator
* Thumbnail Text Generator
* SEO Keyword Analyzer
* Multi-language Support
* Video Idea Generator

---

## 👨‍💻 Author

Ritik Singh

Built as an AI-powered YouTube Content Creation Assistant using Streamlit and Google Gemini AI.
