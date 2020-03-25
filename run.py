from apscheduler.schedulers.blocking import BlockingScheduler
from corona_brasil import Coronavirus_WorldOmeter
from datetime import datetime
import numpy as np
import tweepy 

cons_key, cons_secret, acc_token, acc_secret = np.loadtxt('API_TOKEN.txt', dtype='str', unpack=True)

auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(acc_token, acc_secret)
api = tweepy.API(auth)

def run():
    """Running the coronavirus bot.
    """
    bot = Coronavirus_WorldOmeter()
    bot.get_data()    
    with open('temp.txt', 'w') as f:
        f.write(bot.update())
    
    with open('temp.txt','r') as f:
        api.update_status(f.read())

def run_text():
    now = datetime.now() 
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    T = f"Lembrem-se: \nHigienize as mãos com água e sabão, ou alcool em gel se tiver fora de casa, por pelo menos 20 segundos! \n {dt_string}"
    with open('temp.txt', 'w') as f:
        f.write(T)
    
    with open('temp.txt','r') as f:
        api.update_status(f.read())

if __name__ == '__main__':
    scheduler = BlockingScheduler()    
    scheduler.add_job(run,  'cron', hour='7-23')    
    scheduler.add_job(run_text,  'cron', hour='7-23', minute='30')
    scheduler.start()    
