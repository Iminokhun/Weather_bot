from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot

bot_key = TeleBot('5940200666:AAEewUo1sodfzTuzzeZdY5priEGRbVmxJRg', parse_mode='HTML')

bot = TeleBot(settings.bot_key, threaded=False)



class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.infinity_polling()