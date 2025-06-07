# 🎬 Telegram Screenshot Bot

A Python-based Telegram bot that logs into **HD Film Cehennemi**, captures a screenshot, and sends it to your Telegram chat upon the `/screen` command.

Built using:
- 🐍 Python
- 🤖 Telegram Bot API
- 🧭 Selenium WebDriver (headless Chromium)

---

## 📸 Features

- `/screen` command: Log in and screenshot HD Film Cehennemi homepage or dashboard.
- Sends the screenshot back to the chat where the command was issued.
- Uses headless Chromium for fast and silent operation.
- Credentials stored securely via environment variables.

---

## 🧰 Requirements

- Python 3.7+
- Telegram bot token (via [@BotFather](https://t.me/BotFather))
- Chromium or Google Chrome
- Compatible version of ChromeDriver *(optional with Selenium 4.6+)*

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KananGurbanov/br-tg-bot.git
cd br-tg-bot
```

### 2. Install Python packages and run the app

```bash
python -m venv venv
venv\Scripts\activate         # on Windows
pip install -r requirements.txt
python main.py
