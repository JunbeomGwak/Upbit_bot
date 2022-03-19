import time
import webbrowser
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.jobstores.base import JobLookupError

sched = BackgroundScheduler()
sched.start()

def job():
    print("job function called!!")
    #url= "https://www.google.co.kr/search?q=national+park&source=lnms&tbm=nws"
    #webbrowser.open(url) # Google 뉴스에서 'national park' 검색결과
    
# 매일 특정 HH:MM 및 다음 HH:MM:SS에 작업 실행
sched.add_job(job(), "cron", minute="24", second="01", id="test_1")