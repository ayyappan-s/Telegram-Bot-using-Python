import requests
import telegram
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters

update = Updater("Your Telegram API KEY")

dispatcher = update.dispatcher
global i
i = 0


def greet(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="""
    Hi, I'm a bot. What information you need related to covid
    I can give you the following information
    1.Tips
    2.Statistics(Only for India )
    3.Details about Vaccines
    """)


com_handler = CommandHandler("start", greet)


def message(update, context):
    global i
    splitted_msg = update.message.text.lower().split()


    tips = [
                """<b> Wash your hands frequently and carefully </b>
                 
                      Use warm water and soap and rub your hands for at least 20 seconds. Work the lather to your wrists, between your fingers, and under your fingernails. You can also use an antibacterial and antiviral soap.    
                      Use hand sanitizer when you cannot wash your hands properly. Rewash your hands several times a day, especially after touching anything, including your phone or laptop.     
                     
                For more tips send "more"
                """,
                """<b>Avoid touching your face</b>
                <b>SARS-CoV-2</b> can live on some surfaces for up to 72 hours.
                You can get the virus on your hands 
                if you touch a surface like:
                 
                   gas pump handle     
                   your cell phone    
                   a doorknob    
                  
                Avoid touching any part of your face or head, including your mouth, nose, and eyes. Also avoid biting your fingernails. 
                This can give <b>SARS-CoV-2</b> a chance to go from your hands into your body.
                """,
                """<b>Stop shaking hands and hugging people — for now</b>
                Similarly, avoid touching other people. Skin-to-skin contact can transmit <b>SARS-CoV-2</b> from one person to another
                """,
                """<b>Don’t share personal items</b>
                Do not share personal items like:
                    phones
                    makeup
                    combs 
                """,
                """<b>Cover your mouth and nose when you cough and sneeze </b>
                SARS-CoV-2 is found in high amounts in the nose and mouth. This means it can be carried by air droplets to other people when you cough, sneeze, or talk. It can also land on hard surfaces and stay there for up to 3 days.
                Use a tissue or sneeze into your elbow to keep your hands as clean as possible. Wash your hands carefully after you sneeze or cough, regardless. 
                """,
                """<b>Clean and disinfect surfaces</b> Use alcohol-based disinfectants to clean hard surfaces in your home like:
                    countertops
                    door handles
                    furniture
                    toys """,

            ]
    for msg in splitted_msg:
        if msg in ["tips", "tip", "protection", "secure", "prevention","prevent"]:
                        context.bot.send_message(chat_id=update.message.chat_id, text=tips[0],parse_mode=telegram.ParseMode.HTML)

        if msg in ["hi", "hello", "hai", "good morning"]: greet(update, context)
        if msg == "more":
            if i >= 4:
               context.bot.send_message(chat_id=update.message.chat_id, text="Follow the above steps to prevent you from corona")
            else:

                i = i + 1
                context.bot.send_message(chat_id=update.message.chat_id, text=tips[i], parse_mode=telegram.ParseMode.HTML)


        if msg in ["vaccine", "vaccines", "amtibiotics", "antibodies", "antivirus", "medicines"]:
            context.bot.send_message(chat_id=update.message.chat_id, text='AstraZeneca-Oxford and Bharat Biotech')
        if msg in ["death", "deathrate", "died"]:
            URL = "https://api.covid19api.com/total/country/india"
            r = requests.get(URL)
            data = r.json()
            death_val = data[-1]['Deaths']
            context.bot.send_message(chat_id=update.message.chat_id, text=death_val)
        if msg in ["positive", "affected", "admitted", "cases", "confirmed"]:
            URL = "https://api.covid19api.com/total/country/india"
            r = requests.get(URL)
            data = r.json()
            active_val = data[-1]['Active']
            context.bot.send_message(chat_id=update.message.chat_id, text=active_val)
        if msg in ["total", "affected"]:
            URL = "https://api.covid19api.com/total/country/india"
            r = requests.get(URL)
            data = r.json()
            conf_val = data[-1]['Confirmed']
            context.bot.send_message(chat_id=update.message.chat_id, text=conf_val)
        if msg in ["recovered"]:
            URL = "https://api.covid19api.com/total/country/india"
            r = requests.get(URL)
            data = r.json()
            rec_val = data[-1]['Recovered']
            context.bot.send_message(chat_id=update.message.chat_id, text=rec_val)

msg_handler = MessageHandler(Filters.text, message)

dispatcher.add_handler(com_handler)
dispatcher.add_handler(msg_handler)

update.start_polling()
