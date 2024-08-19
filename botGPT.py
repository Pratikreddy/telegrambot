import logging
from os import environ as env
from dotenv import load_dotenv

import telebot
from openai import OpenAI

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

load_dotenv()
bot = telebot.TeleBot(env["BOT_API_KEY"])
user_id = int(env["USER_KEY"])

def gpt(system_prompt, user_prompt, expected_format, gptkey, model="gpt-4o"):
    client = OpenAI(api_key=gptkey)
    chat_completion, *_ = client.chat.completions.create(
        messages=[
            {"role": "system", "content": f"system_prompt : {system_prompt}"},
            {"role": "user", "content": f"user_prompt : {user_prompt}"},
            {"role": "user", "content": f"expected_JSON_format : {expected_format}"}
        ],
        model=f"{model}",
        response_format={"type": "json_object"},
    ).choices

    content = chat_completion.message.content
    return content

@bot.message_handler(func=lambda message: True)
def get_response(message):
    if int(message.chat.id) != user_id:
        bot.send_message(message.chat.id, "This bot is not for public but private use only.")
    else:
        model = ""
        system_prompt = "You are a helpful assistant."
        expected_format = "plain text"
        
        if message.text.startswith(">>>"):
            model = "gpt-4o-2024-08-06"
            user_prompt = f'```\n{message.text[3:]}\n```'
            expected_format = "code completion"
        elif "code" in message.text.lower() or "python" in message.text.lower():
            model = "gpt-4o-2024-08-06"
            user_prompt = f'"""\n{message.text}\n"""'
            expected_format = "code completion"
        else:
            model = "gpt-4o-mini"
            user_prompt = message.text

        response = gpt(system_prompt, user_prompt, expected_format, env["OPENAI_API_KEY"], model)

        bot.send_message(message.chat.id, response, parse_mode="None")

bot.infinity_polling()
