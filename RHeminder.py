from datetime import datetime
import csv
from telegram import Bot, Update
import asyncio
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes
from exam import new_event

bot_token = '6730302326:AAEUPz1pT-x4QpqpwXA9mUdcFgSVw3yj0lo'
id_list = []

bot = Bot(token=bot_token)

#incomplete function
async def ics_add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    #Somehow the bot can recieve file from user -> file name f"{user_id}.ics"

    new_event(f"{user_id}.ics", user_id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="File uploaded successfully!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global id_list
    user_id = update.message.from_user.id
    id_list.append(user_id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"I'm a bot, your ID is {user_id}!")

async def send_reminder(id, event_name, start, end):
    message = f"Hello! This is your reminder for the event: {event_name} from {start} to {end}."
    await bot.send_message(chat_id=id, text=message)

async def check_events(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id not in id_list:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Please use /start to bein!")
        return

    time_reminder = datetime.strptime("21:46", '%H:%M').time()
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Running Checks")
    while True:
        if str(datetime.now().time())[:5] == str(time_reminder)[:5]:
            for id in id_list:
                with open(f"events_{id}.csv", 'r') as csv_file:
                    reader = csv.DictReader(csv_file)   
                    for row in reader:
                        event_name = row['Event']
                        start = datetime.strptime(row['Start'], '%Y/%m/%d %H:%M:%S')
                        start_date = start.date()
                        end = datetime.strptime(row['End'], '%Y/%m/%d %H:%M:%S')
                        end_date = end.date()
                        
                        if start_date <= datetime.now().date() <= end_date:
                            asyncio.create_task(send_reminder(id, event_name, start, end)) 

            await asyncio.sleep(60)
        application.run_polling()

application = ApplicationBuilder().token('6730302326:AAEUPz1pT-x4QpqpwXA9mUdcFgSVw3yj0lo').build()
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)
event_handler = CommandHandler('check', check_events)
application.add_handler(event_handler)
upload_handler = CommandHandler('upload', ics_add)
application.add_handler(upload_handler)

while True:
    application.run_polling()

        
