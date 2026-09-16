# Telegram Reminders

A small personal automation that sends a scheduled Telegram reminder on the last Thursday of each month. I built it for my own recurring reminder workflow, but the setup is generic enough to reuse for other private notifications.

## The problem

A monthly reminder is easy to forget when it depends on a calendar rule rather than a fixed date. Checking the calendar manually every month adds friction and makes the process unreliable.

## The solution

The project combines a short Python script with GitHub Actions. The workflow runs every Thursday, the script checks whether the current day is the last Thursday of the month, and only then sends a Telegram message.

## How it works

1. GitHub Actions starts the workflow at 07:00 UTC every Thursday.
2. `send_message.py` checks whether the next Thursday belongs to another month.
3. If today is the last Thursday, the script sends the reminder through the Telegram Bot API.
4. The bot token and destination chat ID are read from environment variables or GitHub Secrets.

## Setup

### 1. Create a Telegram bot

Create a bot through [@BotFather](https://t.me/BotFather) and save the generated token. Start a conversation with the bot and obtain the destination chat ID through the Telegram Bot API.

### 2. Configure GitHub Secrets

Add these repository secrets under **Settings > Secrets and variables > Actions**:

- `TELEGRAM_BOT_TOKEN`;
- `TELEGRAM_CHAT_ID`.

Never put either value in the repository, README, workflow file, or command history.

### 3. Run locally

```bash
pip install -r requirements.txt
python send_message.py
```

For local testing, set the variables in the current shell:

```powershell
$env:TELEGRAM_BOT_TOKEN = "your_bot_token"
$env:TELEGRAM_CHAT_ID = "your_chat_id"
python send_message.py
```

### 4. Run through GitHub Actions

Open the repository's **Actions** tab, select the reminder workflow, and use **Run workflow** for a manual test. Scheduled runs happen every Thursday; a message is sent only on the last Thursday of the month.

## Project structure

```text
send_message.py                 # Date rule and Telegram API call
requirements.txt                # Python dependencies
.github/workflows/last_thursday.yml
                                # Scheduled GitHub Actions workflow
```

## Security

All credentials are injected at runtime. If a bot token is ever exposed, revoke it through BotFather immediately and create a replacement.

## License

This personal automation is available under the [Creative Commons Attribution-NonCommercial 4.0 International license](LICENSE). Attribution to Loginov Gleb is required; commercial use requires prior written permission.
