import logging
import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import Config
from handlers.start import setup_start_handlers
from handlers.menu import setup_menu_handlers
from handlers.thumbnail_extractor import setup_thumbnail_handlers
from handlers.caption_editor import setup_caption_handlers
from handlers.metadata_editor import setup_metadata_handlers
from handlers.progress import setup_progress_handlers

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    # Create directories
    os.makedirs(Config.DOWNLOAD_PATH, exist_ok=True)
    os.makedirs(Config.UPLOAD_PATH, exist_ok=True)
    os.makedirs(Config.THUMBNAIL_DIR, exist_ok=True)
    os.makedirs(Config.METADATA_DIR, exist_ok=True)
    
    # Create Telegram application
    application = Application.builder().token(Config.BOT_TOKEN).build()
    
    # Set up handlers
    setup_start_handlers(application)
    setup_menu_handlers(application)
    setup_thumbnail_handlers(application)
    setup_caption_handlers(application)
    setup_metadata_handlers(application)
    setup_progress_handlers(application)
    
    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
