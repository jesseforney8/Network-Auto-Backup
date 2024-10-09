from main_gui import search_db, update_record1, refresh_view
from net_backup import back_up
from datetime import datetime
import time

#automatic back ups daily at midnight
def auto_back_up():
    is_running = True
    while is_running:
        time.sleep(3)
        print("auto backup is running!")
        #check time
        now = datetime.now()
        now = str(now)
        now = now.rsplit(" ")
        now[1] = now[1][0:2]
        now[0] = now[0][-2:]
        t = now[1]

        #if time is 12 then back up

        if t == "23":

            #for every entry, back up
            for d in search_db():
                try:
                    back_up(d[1], d[2], d[3], d[4], d[5], datetime.now())
                    print("backed up!")
                except:
                    print("failed backed up!")
                
                update_record1(id=d[9], date1=datetime.now())
                refresh_view()
            time.sleep(3600)