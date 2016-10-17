# -*- coding: utf-8 -*-
from twx.botapi import TelegramBot

"""
Setup the bot
"""

bot = TelegramBot('279618993:AAE2-wl3HOeOEd8RjCiLkIkBP_YLlMAFyFY')
bot.update_bot_info().wait()

"""
Get updates sent to the bot
"""
updates = bot.get_updates().wait()
text = updates[-1].message.text
user_id = updates[-1].message.sender.id

bot.send_message(user_id, 'jaja xd').wait()