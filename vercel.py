import os
import openai
import telebot

# 从环境变量中读取 OpenAI API 密钥和 Telegram 机器人令牌
openai.api_key = os.environ.get('OPENAI_API_KEY', '')
bot_token = os.environ.get('TELEGRAM_BOT_TOKEN', '')

# 设置 OpenAI API 基本 URL
openai.api_base = "https://chimeragpt.adventblocks.cc/api/v1"

# 初始化 Telegram 机器人
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "你好！我是由 GPT-3.5 Turbo 驱动的助手。发送消息给我，我会回复你的！")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # 获取用户输入
    user_input = message.text

    # 调用 GPT-3.5 Turbo API 生成回复
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': user_input},
        ]
    )

    # 提取 AI 的回复
    ai_response = response['choices'][0]['message']['content']

    # 将 AI 的回复发送回给用户
    bot.reply_to(message, ai_response)

if __name__ == "__main__":
    bot.polling()
