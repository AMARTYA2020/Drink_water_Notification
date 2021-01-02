import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title = "Please drink water",
            message="Fluids and hydration are crucial for the bodily functions of humans, especially when it comes to drinking water. As you probably remember, 60-80 percent of the human body is water. ",
            app_icon=r"C:\Users\AMARTYA PANDEY\PycharmProjects\Drink_water_Notification\icon.ico",
            timeout=10
        ) 
        time.sleep(60*60)  # We will be notified every hour ! That's impressive just similar to setting an Alarm clock while we are constantly working


