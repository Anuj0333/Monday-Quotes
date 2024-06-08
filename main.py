
# Sending Emails

# import smtplib
# my_email="guptaanuj0812"
# passward="gqqtssunqymavwrp"
# with smtplib.SMTP("smtp.gmail.com") as connection
#     connection.starttls()
#     connection.login(user=my_email,password=passward)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="anujgupta0333@gmail.com",
#                         msg="Subject:Hello\n\nthis is me")



# import datetime as dt

# now=dt.datetime.now()
# year=now.year
# month=now.month
# day_of_week=now.weekday()
# print(day_of_week)


# date_of_birth=dt.datetime(year=2002,month=12,day=8)
# print(date_of_birth)



import smtplib
import datetime as dt
import random

my_email="guptaanuj0812"
password="gqqtssunqymavwrp"

now=dt.datetime.now()
week_day=now.weekday()
if week_day==0:
    with open("C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/Birthday wishes/Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote=random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs="anujgupta0333@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}")
