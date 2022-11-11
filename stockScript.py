from bs4 import BeautifulSoup
import requests
from email.message import EmailMessage
import ssl
import smtplib
import time
import os
from dotenv import load_dotenv

load_dotenv()

context = ssl.create_default_context()

sender = os.getenv("MAIL")
password = os.getenv("PASSWORD")
receiver = "emirdlcn@gmail.com"

def initialization_mail():
    em = EmailMessage()
    em["From"] = sender
    em["To"] = receiver
    em["subject"] = "nike-dunk stok takibi"
    em.set_content("https://shopigo.com/products/nike-dunk-low-retro-white-black-1\nYukarıdaki link için stok geldiğinde bilgilendirme maili alacaksınız.")
    smtp.sendmail(sender,receiver,em.as_string())

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(sender,password)
    initialization_mail()
    while(True):
        html = requests.get("https://shopigo.com/products/nike-dunk-low-retro-white-black-1").text
        bs = BeautifulSoup(html,"html.parser")
        res = bs.find(class_ ="add-to-card-btn").getText().strip()
        if (res == "SEPETE EKLE"):
            em = EmailMessage()
            em["From"] = sender
            em["To"] = receiver
            em["subject"] = "nike-dunk stok güncellemesi"
            em.set_content("https://shopigo.com/products/nike-dunk-low-retro-white-black-1\nStok yenilendi, acele edin.")
            smtp.sendmail(sender,receiver,em.as_string())
        elif res == "YAKINDA":
            print(res)

        time.sleep(20)
            

