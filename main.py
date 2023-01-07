from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.uic import loadUi
import sqlite3

import smtplib
import config
import sys

connect = sqlite3.connect('users.sql')
cur  = connect.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(255),
    theme VARCHAR(255),
    message VARCHAR(255)

    );
    """)
connect.commit()

class Form(QMainWindow):
    def __init__(self):
            super(Form,self).__init__()

            loadUi("untitled.ui",self)
            self.push.clicked.connect(self.button_send)

    def button_send(self):
        try:
            komu = str(self.komu.text())
            tema = str(self.tema.text())
            sms = str(self.sms.text())
            cur  = connect.cursor()
            cur.execute(f"INSERT INTO users VALUES ('{komu}', {tema}, {sms});")
            connect.commit()
            
            
            sender = config.sender
            password = config.password
            

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender,password)
            server.sendmail(sender, komu, f"Subject: {tema} \n\n{sms}")
            self.loading.setText("Отправлено!")

        except:
            self.loading.setText("Произошла ошибка, повторите попытку!")


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
