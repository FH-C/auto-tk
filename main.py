import sys

from apscheduler.schedulers.blocking import BlockingScheduler

from crawler import crawl
from utils import init_logger

if __name__ == '__main__':
    init_logger()
    if len(sys.argv) == 1:
        scheduler = BlockingScheduler()
        scheduler.add_job(crawl, 'cron', day_of_week='0', hour=10, minute=0)
        scheduler.start()
    else:
        crawl()
