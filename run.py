from apscheduler.schedulers.blocking import BlockingScheduler
from corona_brasil import Coronavirus

def run():
    """Running the coronavirus bot.
    """
    bot = Coronavirus()
    bot.get_data()
    print(bot)

scheduler = BlockingScheduler()
scheduler.add_job(run, 'interval', minutes=1)
scheduler.start()