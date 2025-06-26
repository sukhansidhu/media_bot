# Media Bot

A Telegram bot with various media processing capabilities.

## Features
- Thumbnail extraction
- Caption and button editing
- Metadata editing
- Video conversion
- Video trimming and merging
- Stream extraction and removal
- And many more!

## Deployment

### Local Setup
1. Clone the repository: `git clone https://github.com/yourusername/media-bot.git`
2. Create `.env` file: `cp .env.example .env`
3. Edit `.env` with your bot token
4. Install dependencies: `pip install -r requirements.txt`
5. Run the bot: `python main.py`

### Docker
```bash
docker build -t media-bot .
docker run -d --name media-bot -e BOT_TOKEN=your_token media-bot
