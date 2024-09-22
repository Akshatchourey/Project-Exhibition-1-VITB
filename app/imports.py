import os
import random
import pymysql
import tkinter as tk
from tkinter import ttk
from smtplib import SMTP
from dotenv import load_dotenv
from PIL import Image, ImageTk
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

load_dotenv()
timeout = 10
db = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="money",
    host=os.environ.get('DB_HOST'),
    password=os.environ.get('DB_PASSWORD_DEFAULT'),
    read_timeout=timeout,
    port=12727,
    user=os.environ.get('DB_USER_DEFAULT'),
    write_timeout=timeout,
)
def switch_user(username, password):
    global db
    try:
        db = pymysql.connect(
            charset="utf8mb4",
            connect_timeout=timeout,
            cursorclass=pymysql.cursors.DictCursor,
            db="money",
            host=os.environ.get('DB_HOST'),
            password=password,
            read_timeout=timeout,
            port=12727,
            user=username,
            write_timeout=timeout,
        )
        print("Connection successfully...for user", db.user.decode("utf-8"))
        return 0

    except pymysql.Error as e:
        print("invalid credentials.")
        return 1
def database():
    return db

# pip install python-dotenv
