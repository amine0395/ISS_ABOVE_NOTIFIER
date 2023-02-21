import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
MY_EMAIL="@gmail.com"# Your Bot email that he'll be using to mail your destination
MY_PASSWRD="XXXXXXXX"#Replace with your bot email password so he can access it
EMAIL_DEST="@gmail.com"#Your Destination email that will recieve whether
                       # or not the iss is above that inserted lontitude/lagithude
while True:

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])



    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour<sunrise or time_now.hour>sunset :
        if MY_LAT-5<=data["iss_position"]["latitude"]<=MY_LAT+5 and MY_LONG-5<=data["iss_position"]["longitude"]<=MY_LONG+5 :
            myemail = MY_EMAIL
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=myemail, password=MY_PASSWRD)
            connection.sendmail(from_addr=myemail, to_addrs=EMAIL_DEST, msg="The iss is above your head \n \n ")
            connection.close()
        else:
            print("no iss above you right now sorry")
    else:
        print("you can't see it it's day")

    time.sleep(60)

