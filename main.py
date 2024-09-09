# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper

from flask import Flask
import threading
from bot import Bot

backapp = Flask(__name__)

@backapp.route('/', methods=['GET'])
def health_check():
    return 'OK', 200

def run_flask():
    backapp.run(host="0.0.0.0", port=8000)

def runbot():
    app = Bot()
    app.run()

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    runbot()






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
