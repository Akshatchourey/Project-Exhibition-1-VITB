import os
import numpy as np
import mysql.connector
from Database import Abc
from smtplib import SMTP_SSL as SMTP


def send_code(code):
    username = 'shoryapathak07@gmail.com'
    password = "Shorya9528**!!?"
    to = ['achourey09@gmail.com']
    subject = "Verify yourself Please."
    conn = SMTP('smtp.gmail.com')
    conn.set_debuglevel(False)
    print("No yar")
    conn.login(username, password)
    try:
        # msg = MIMEText(content, 'plain')
        # msg['Subject'] = subject
        # msg['From'] = sender


        try:
            # msg.as_string()
            conn.sendmail(username, to, code)
        finally:
            conn.quit()

    except:
        print("mail failed.")

    # 587
    # server.starttls()


if __name__ == "__main__":
    # arr_2D = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    # send_code(2252)
    try:
        timeout = 10
        db = pymysql.connect(
            charset="utf8mb4",
            connect_timeout=timeout,
            cursorclass=pymysql.cursors.DictCursor,
            db="money",
            host=os.environ.get('DB_HOST'),
            password=os.environ.get('DB_PASSWORD_ROOT'),
            read_timeout=timeout,
            port=12727,
            user=os.environ.get('DB_USER_ROOT'),
            write_timeout=timeout,
        )
        print("Connection successfully...")

    except pymysql.Error as e:
        print(f"Connection failed: {e}")

    db.close()


