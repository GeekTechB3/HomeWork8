# 1) Напишите программу для отправки почты через PyQt5.
# Используйте технологии SMTP, PyQt5и sqlite3. Сделайте базу для программы
# на основе sqlite3. То есть каждое сообщение которое мы отправляем мы
# записываем в Базу Данных (кому, тема, сообщение, дата).
# Примерный дизайн программы:

from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.uic import  loadUi
import sqlite3
import smtplib
import config
import sys

connect = sqlite3.connect('users.db')
cur  = connect.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(255),
    theme VARCHAR(255),
    message VARCHAR(255)

    );
    """)
connect.commit()

class Form(QDialog):
    def __init__(self):
            super(Form, self).__init__()


            loadUi('HW.ui',self)
            self.send.clicked.connect(self.button)


    def button(self):
        try:
            komu = str(self.komu.text())
            tema = str(self.tema.text())
            sms = str(self.sms.text())
            sender = config.sender
            password =config.password
            cur  = connect.cursor()
            cur.execute(f"INSERT INTO users VALUES ('{komu}', '{tema}', '{sms}');")
            connect.commit()


            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender,password)
            server.sendmail(sender, komu,  f'Subject: {tema}  \n\n {sms}')
            self.sms.setText("Рассылка отправлена! ")


        except :
                self.sms.setText("Произошла ошибка, повторите попытку!")



app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()


