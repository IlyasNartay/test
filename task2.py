import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

folder_path = "Раздаточный материал 1\\Файлы заказчика\\"
files = os.listdir(folder_path)

# Запись названий файлов в блокнот
with open("Файлы_заказчика.txt", "w", encoding="utf-8") as file:
    for f in files:
        file.write(f + "\n")

# Поиск файла с наибольшим весом
max_size = 0
max_file = ""
for f in files:
    size = os.path.getsize(os.path.join(folder_path, f))
    if size > max_size:
        max_size = size
        max_file = f

# Отправка email
sender = os.getenv("EMAIL")
receiver = "ilyas.nartay@gmail.com"
password = os.getenv("PASSWORD")

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = "Список файлов"

body = f"Список файлов прикреплен.\nФайл с наибольшим весом: {max_file} ({max_size} байт)"
msg.attach(MIMEText(body, "plain"))

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())