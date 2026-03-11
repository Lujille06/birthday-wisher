import datetime
import random
import pandas
from smtplib import SMTP
import os

date = datetime.datetime.now()

with open("birthdays.csv") as birthdays:
    df = pandas.read_csv(birthdays)

for index, row in df.iterrows():

    if row["month"] == date.month and row["day"] == date.day:

        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", encoding='utf-8') as letter:
            lines = letter.read()
            updatedLetter = lines.replace("[NAME]", row["name"])

        MY_EMAIL = os.environ.get("MY_EMAIL")
        MY_PASSWORD = os.environ.get("MY_PASSWORD")
        
        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()

            connection.login(user=MY_EMAIL, password=MY_PASSWORD)

            connection.sendmail(from_addr=MY_EMAIL, to_addrs=row["email"], msg=f"Subject:Happy Birthday! \n\n {updatedLetter}".encode('utf-8'))
