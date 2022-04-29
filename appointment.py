from datetime import date,timedelta
import datetime
import time
today=date.today()
datelist=[(datetime.date(2021,4,2),datetime.date(2021,4,5),datetime.date(2021,4,10))]
diary=("10 am Birthday party at tiruchy","11 am Meeting at tirunelveli","9 am Function at madurai")
def display():
    sd=raw_input("Enter the start date(dd/mm/yyyy):")
    se=raw_input("Enter the end   date(dd/mm/yyyy):")
    d1=sd.split('-')
    d2=se.split('-')
    date1=datetime.date(int(d1[0]),int(d1[1]),int(d1[2])) 
    date2=datetime.date(int(d2[0]),int(d2[1]),int(d2[2]))
    delta=date2-date1
    for j in range(2):
        for i in range(delta.days+1):
            day=date1+timedelta(days=i)
            if(day==datelist[j]):
                if day>today:
                    difference=(day-today).days
                else:
                    difference=(today-day).days
                    print(day,diary[j],difference,'more')
display()
                        
                        
