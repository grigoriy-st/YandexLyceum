import time
import schedule
from datetime import datetime

def ku():
    cur_h = datetime.now().hour
    print("Ку" * cur_h)

schedule.every().hour.at(":55").do(ku)

while True:
    schedule.run_pending()
    time.sleep(1)
