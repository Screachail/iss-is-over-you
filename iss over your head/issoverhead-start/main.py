import requests
from datetime import datetime
import smtplib
import ssl

MY_LAT = 50.869930 # Your latitude
MY_LONG = 20.640961 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


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
hour = time_now.hour
#If the ISS is close to my current position


import time
starttime = time.time()
while True:
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5 and\
            (hour >= sunset or hour <= sunrise):
        ctx = ssl.create_default_context()
        password = "faxxkncxdwovlzqf"  # Your app password goes here
        sender = "bobrowski.stefan.87@gmail.com"  # Your e-mail address
        receiver = "bobrowski_stefan@yahoo.com"  # Recipient's address
        message = f"Subject: ISS is near. \n" \
                f"Look up, the ISS is near you, mate!"
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message)
    else:
        print("ISS is not here yet :(")
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))


# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



