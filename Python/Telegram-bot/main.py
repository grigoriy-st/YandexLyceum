import logging
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    filters,
    CommandHandler,
    ContextTypes,
    CallbackContext
)
from config import BOT_TOKEN
from datetime import datetime
from zoneinfo import ZoneInfo

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

def remove_job_if_exists(name, context):
    if not context.job_queue:
        return False
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True

async def set_timer(update, context):
    try:
        seconds = int(context.args[0])
        if seconds <= 0:
            await update.message.reply_text("Время должно быть больше 0!")
            return

        chat_id = update.effective_message.chat_id
        job_removed = remove_job_if_exists(str(chat_id), context)

        context.job_queue.run_once(
            timer_callback,
            seconds,
            chat_id=chat_id,
            name=str(chat_id),
            data=seconds
        )

        text = f'Таймер установлен на {seconds} секунд!'
        if job_removed:
            text += ' Предыдущий таймер удален.'
        await update.message.reply_text(text)

    except (IndexError, ValueError):
        await update.message.reply_text("Используйте: /set_timer <секунды>")

async def timer_callback(context):
    seconds = context.job.data
    await context.bot.send_message(
        context.job.chat_id,
        text=f'Таймер на {seconds} секунд сработал!'
    )

async def unset_timer(update, context):
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = 'Таймер отменен!' if job_removed else 'Нет активных таймеров'
    await update.message.reply_text(text)

async def echo(update, context):
    msg = update.message.text
    await update.message.reply_text(f'Я получил сообщение {msg}')

async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(rf'Привет {user.mention_html()}! Я бот!')

async def help_command(update, context):
    await update.message.reply_text("Помощь: /set_timer <секунды>")

async def get_time(update, context):
    o_time = datetime.now(ZoneInfo('Asia/Omsk'))
    await update.message.reply_text(f'Сейчас: {o_time.strftime("%H:%M:%S")}')

async def get_date(update, context):
    o_time = datetime.now(ZoneInfo('Asia/Omsk'))
    await update.message.reply_text(f'Сегодня: {o_time.strftime("%d.%m.%Y")}')

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("time", get_time))
    application.add_handler(CommandHandler("date", get_date))
    application.add_handler(CommandHandler("set_timer", set_timer))
    application.add_handler(CommandHandler("unset_timer", unset_timer))

    application.run_polling()

if __name__ == '__main__':
    main()
