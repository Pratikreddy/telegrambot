GPT Telegram Bot
Script for a Telegram bot that uses OpenAI API similar to ChatGPT. It has all its capabilities plus the fact that by using the API directly, there is no waiting time prior to using this bot. The current downside to this project is that the script has to be running for the bot to work. Anyone willing to contribute to this project in anyway, particularly by making it work forever, please visit the Contribution section.

Features
 Use OpenAI API through Telegram
 Get text replies by default
 Get code responses by starting your messages with >>>
 Get code related answers by using the word code in your meessage
 Make your bot private for personal use
How to install
1. Install Python
Get Python installed in the most recent version together with the following packages:

pip install openai
pip install pyTelegramBotAPI
pip install python-dotenv
2. Install Telegram
If you do not already have Telegram in any device or web browser, create an account as it is needed.

3. Create an OpenAI account
If you do not already have an account, create one at OpenAI website.

4. Gather your keys
Once you have your Telegram and OpenAI accounts, gather the keys.

OpenAI API key:

Log-in in OpenAI keys
Create a new secret key and copy it to the clipboard. This is your OPENAI_API_KEY. It should look like this: xx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Paste it in your .env file in the field OPENAI_API_KEY
Set! Be aware that you will be using your own OpenAI credit so charges might be applied.
Telegram Bot key:

Open Telegram in any of your devices
Open a chat with @BotFather. It is your go-to for all things bot, from creation to settings
Type /newbot to begin. The BotFather will ask you to pick a bot name (which must be universally unique) and a username, it then generates an authentication token for your new bot. This token is your BOT_API_KEY. It should look like this: 0123456789:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Paste it in your .env file in the field BOT_API_KEY
Done!
Telegram user key:

Head back to Telegram and open a chat with @userinfobot
Type /start to begin. It will reply with your info.
Copy the ID, that should look like this: 0123456789
Paste it in your .env file in the field USER_KEY
Nice! This way only you can talk with the bot. Notice that if you would like the bot to reply to many people you should modify the code to stop rejecting other peoples' messages.
Make sure your .env file has the three KEYs obtained during this step. Save the file. It might dissapear but it is still there.

5. Decide which engine suits you
The script is intended to be used for natural and code responses, if either the message starts with >>> or contains code or python keywords. If you are willing to use other engine rather than the ones included, just change it by the one that suits you. Not sure on which engine suits you? Check the official website to see what each model offers here.

6. Run the script
Now you can use the bot as long as the script is running. Just type Hello! and make sure it responds.
