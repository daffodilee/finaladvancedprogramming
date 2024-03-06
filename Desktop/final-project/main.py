from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters, CallbackContext
import joblib




# Load your trained model and vectorizer
model = joblib.load('spam_classifier_model.joblib')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.joblib')

bot_active = True

def start(update: Update, context: CallbackContext) -> None:
    """Sends a message when the command /start is issued."""
    global bot_active
    bot_active = True
    update.message.reply_text('Hi! I am your spam filter bot. Send me a message and I will tell you if it is spam or not!')

def help_command(update: Update, context: CallbackContext) -> None:
    """Sends a message when the command /help is issued."""
    update.message.reply_text('Just send me any text and I will analyze it for you!')

def analyze_message(update: Update, context: CallbackContext) -> None:
    """Analyze the text message."""
    global bot_active
    if not bot_active:
        return
    text = update.message.text
    input_data_features = tfidf_vectorizer.transform([text])
    prediction = model.predict(input_data_features)
    
    if prediction[0] == 1:
        response = "This message is not spam."
    else:
        response = "This message is spam!"
    
    update.message.reply_text(response)

def stop(update: Update, context: CallbackContext) -> None:
    """Sends a message when the command /stop is issued."""
    global bot_active
    bot_active = False
    update.message.reply_text('Bot stopped. Send /start to launch the bot again.')

def main():
    """Start the bot."""
    # Replace 'YOUR_TOKEN' with the token given by BotFather
    updater = Updater("6652446402:AAE5DOnsPwxVPGQgoN8jhniZi6aLVxaWH4Q", use_context=True)

    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("stop", stop))

    # on non-command i.e. message - analyze the message
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, analyze_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()