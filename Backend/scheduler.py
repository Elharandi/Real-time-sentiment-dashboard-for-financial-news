from apscheduler.schedulers.background import BackgroundScheduler
from pipeline import fetch_score_and_store

scheduler = BackgroundScheduler()

scheduler.add_job(fetch_score_and_store, 'interval', minutes=60)
scheduler.start()






