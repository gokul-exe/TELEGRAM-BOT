import toml
import telegram
from telegram import BotCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from csvdata import save_user
from  responses import resp_collec



commands = [
    BotCommand(command="/start", description="Start the bot"),
    BotCommand(command="/help", description="to know about the functions"),
    BotCommand(command="/stop", description="Stop using the bot")
    # Add more commands as needed 
    ]

bot_running = True  # Flag to track the bot's state

def start_command(update, context):
    chat_id = update.effective_chat.id
    username = update.effective_user.full_name
    save_user(chat_id, username)
    global bot_running
    if not bot_running:
        bot_running = True  # Set the bot state to running
        update.message.reply_text("Bot started. Welcome back!")
    else:
        update.message.reply_text("Bot is already running.")

def stop_command(update, context):
    global bot_running
    if bot_running:
        bot_running = False  # Set the bot state to stopped
        update.message.reply_text("Bot stopped. Use /start to run the bot again.")
    else:
        update.message.reply_text("Bot is already stopped.")

def help_command(update, context):    
    update.message.reply_text("""🌐 Translation: Translate text from one English to Tamil(eg:transaltion hi how are you). 

🌦️ Weather: Get the current weather conditions for your location or any specified location.

😄 Meme: Generate random memes for some fun and laughter.

🔍 Image Search: Search for images on the web based on your query.(eg:image Aircraft)

--------------------------------👨‍💻 Created by Gokul-------------------------------""")

    
def handle_message(update, context):
    global bot_running
    if bot_running:       
        text=str(update.message.text).lower()        
        response=resp_collec(text,context,update)
        try :
            update.message.reply_text(response)
        except :
            pass
    else:
        update.message.reply_text("Bot is currently stopped. Use /start to run the bot again.")

def main():
    # Load the API token from the config file
    config = toml.load("config.toml")
    api_token = config["bot"]["api_token"]    
    # Create a bot instance
    bot = telegram.Bot(api_token)    
    # Set the bot's command list
    bot.set_my_commands(commands)    
    updater = Updater(api_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("stop", stop_command))
    dispatcher.add_handler(CommandHandler("help", help_command))    
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))    
    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    main()
