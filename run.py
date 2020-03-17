from apscheduler.schedulers.blocking import BlockingScheduler
from corona_brasil import Coronavirus
import numpy as np
import tweepy 

cons_key, cons_secret, acc_token, acc_secret = np.loadtxt('API_TOKEN.txt', dtype='str', unpack=True)

auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(acc_token, acc_secret)
api = tweepy.API(auth)

def run():
    """Running the coronavirus bot.
    """
    bot = Coronavirus()
    bot.get_data()
    with open('temp.txt', 'w') as f:
        f.write(bot.update())
    
    with open('temp.txt','r') as f:
        api.update_status(f.read())

scheduler = BlockingScheduler()
scheduler.add_job(run,  'cron', hour='7-20')
scheduler.start()