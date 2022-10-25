from telegram.ext import *
import logging
import os
import requests as requests
BOT_TOKEN = os.getenv("5728118676:AAGeC_zi8Zm-KnDNBtL1U6GDJBn3ygayCLs")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
def ex_id(id):
    result=False
    file=open("users.txt",'r')
    for line in file:
        if line.strip()==id:
            result=True
    file.close()
    return result


def start_command(update, context):
    if update.message.chat.type=='private':
         idu=update.message.chat.full_name
         f=open("users.txt","a")
         if(not ex_id(str(idu))):
                f.write("{}\n".format(idu))
                f.close()
         update.message.reply_sticker("CAACAgIAAxkBAAIEd2JZLvjl2AG4exeqftRZrzaJKVAWAAIBAQACVp29CiK-nw64wuY0IwQ")
         update.message.reply_text((
            f'''🔰 Hello Dear, {update.message.chat.full_name} 😊\n\n🛰️ I'm IP FINDER BOT ⚡\n\n🚀 Send Any Ip Address To Me 😎\n\n ⭐ I'm Also IPV6 Supported 🙈'''))

def info_command(update,context):
    file=open("users.txt",'r')
    us=len(file.readlines())
    update.message.reply_text(f'''───────────────\n🚀 Hear is Bot Staticts 🚀\n───────────────\n🔰 Active Users :- {us} ✅\n\n🔄 Bot Version:- 0.1✅ ''')


def get_ip():
    pass

def get_location(ip_address):
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        location_data = {"ip": ip_address,"city": response.get("city"),"region": response.get("region"),"country": response.get("country_name"),"ISP": response.get("org") }
        return(location_data)

def message_info(update,context):
      ip_address = update.message.text
      location_data = get_location(ip_address)
      values = location_data.values()
      value=list(values)
      update.message.reply_text(f'''🛰️IP Address ᗚ {value[0]}\n\n🏠City ᗚ {value[1]}\n\n🗺️Province ᗚ {value[2]}\n\n🌎Country ᗚ {value[3]}\n\n🗼Internet Provider ᗚ {value[4]} ''')



def main() -> None:
    """Run the bot."""
    updater = Updater("5728118676:AAGeC_zi8Zm-KnDNBtL1U6GDJBn3ygayCLs")
    updater.dispatcher.add_handler(CommandHandler("start",start_command, run_async=True))
    updater.dispatcher.add_handler(CommandHandler("info", info_command, run_async=True))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message_info))
    updater.start_polling()

if __name__ == '__main__':
    main()




















