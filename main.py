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
            f'''π° Hello Dear, {update.message.chat.full_name} π\n\nπ°οΈ I'm IP FINDER BOT β‘\n\nπ Send Any Ip Address To Me π\n\n β­ I'm Also IPV6 Supported π'''))

def info_command(update,context):
    file=open("users.txt",'r')
    us=len(file.readlines())
    update.message.reply_text(f'''βββββββββββββββ\nπ Hear is Bot Staticts π\nβββββββββββββββ\nπ° Active Users :- {us} β\n\nπ Bot Version:- 0.1β ''')


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
      update.message.reply_text(f'''π°οΈIP Address α {value[0]}\n\nπ City α {value[1]}\n\nπΊοΈProvince α {value[2]}\n\nπCountry α {value[3]}\n\nπΌInternet Provider α {value[4]} ''')



def main() -> None:
    """Run the bot."""
    updater = Updater("5728118676:AAGeC_zi8Zm-KnDNBtL1U6GDJBn3ygayCLs")
    updater.dispatcher.add_handler(CommandHandler("start",start_command, run_async=True))
    updater.dispatcher.add_handler(CommandHandler("info", info_command, run_async=True))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message_info))
    updater.start_polling()

if __name__ == '__main__':
    main()




















