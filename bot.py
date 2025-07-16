import logging
from telegram import (
    Update, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton
)
from telegram.ext import (
    Application, 
    CommandHandler, 
    CallbackQueryHandler,
    ContextTypes
)

# ===== CONFIGURATION =====
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your actual token
TELEGRAM_LINK = "https://t.me/shekeaglememe"
TWITTER_LINK = "https://x.com/Slothmeme2025"
FACEBOOK_LINK = "https://facebook.com/shekeaglememe"

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ===== HANDLERS =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_msg = (
        "🌟 *Welcome to the ShekeAgleMeme Airdrop!* 🌟\n\n"
        "To qualify for Mr Obafbtc's legendary 100 SOL airdrop, "
        "complete these simple tasks:\n\n"
        "1. Join our Telegram Channel\n"
        "2. Join our Telegram Group\n"
        "3. Follow us on Twitter\n"
        "4. Like our Facebook Page\n\n"
        "Click the buttons below to complete the tasks!"
    )
    
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📢 Telegram Channel", url=TELEGRAM_LINK),
            InlineKeyboardButton("💬 Telegram Group", url=TELEGRAM_LINK)
        ],
        [
            InlineKeyboardButton("🐦 Twitter", url=TWITTER_LINK),
            InlineKeyboardButton("👍 Facebook", url=FACEBOOK_LINK)
        ],
        [InlineKeyboardButton("✅ I've Completed All Tasks", callback_data="completed")]
    ])
    
    await update.message.reply_text(
        welcome_msg, 
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

async def handle_completion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    congratulation_msg = (
        "🎉 *CONGRATULATIONS!* 🎉\n\n"
        "You've successfully qualified for Mr Obafbtc's exclusive airdrop!\n\n"
        "💎 *100 SOL* is now on its way to your wallet!\n\n"
        "We trust you completed all tasks honestly. "
        "Welcome to the ShekeAgleMeme family! "
        "To the moon! 🚀🌕\n\n"
        "PS: Watch your wallet for the surprise!"
    )
    
    await query.message.edit_text(
        congratulation_msg,
        parse_mode="Markdown"
    )

# ===== MAIN SETUP =====
def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_completion, pattern="^completed$"))
    
    logger.info("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
