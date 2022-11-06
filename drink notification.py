'''DRINK WATER NOTIFICATION APP WHICH WILL REMIND US TO DRINK WATER THROUGH NOTIFICATION PERIODICALLY'''

#time import is used to use time related tasks
import time

#this import is used to get notification from the system
from plyer import notification

#main program in this main function
#notify fuction of notification take title,message,appicon,timeout arguement
if __name__ == "__main__":
    while True:
        notification.notify( title = "Time To Drink Water", message = "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.", app_icon = "F:\\ashu backup\Programs\logical programs\drink water reminder\Iconsmind-Outline-Glass-Water.ico", timeout = 5 )
        time.sleep(10)