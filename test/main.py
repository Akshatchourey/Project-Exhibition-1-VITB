import os
import numpy as np
import mysql.connector
from Database import Abc
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Shorya9528**!!?
def send_code(code):
    g_username = "shoryapathak07@gmail.com"
    g_password = 'ucnrddfcamjuospn'
    to = ["shoryapathak787@gmail.com"]
    subject = "Verify yourself Please."

    msg = MIMEMultipart()
    msg['From'] = g_username
    msg['To'] = ", ".join(to)
    msg['Subject'] = subject
    msg.attach(MIMEText(code, 'plain'))
    with SMTP("smtp.gmail.com") as server:
        server.starttls()
        server.login(user=g_username, password=g_password)
        server.sendmail(from_addr=g_username, to_addrs=to,msg=msg.as_string())
        server.close()
        print("Done.")


if __name__ == "__main__":
    # arr_2D = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    # send_code("Your verification code is 468}")
    print("main program")

