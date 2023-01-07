from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys
import sqlite3
import smtplib 
import config

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
        super(Form, self).__init__()

        loadUi('gmail.ui', self)
        
        
        self.send.clicked.connect(self.send_email)

    def send_email(self):
        input1 = str(self.input1.text())
        input2 = str(self.input2.text())
        input3 = str(self.input3.text())
        cur  = connect.cursor()
        cur.execute(f"INSERT INTO users VALUES ('{input1}', {input2}, {input3});")
        connect.commit()


            


        sender = config.sender
        password = config.password


        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, input1, f"Subject: {input2} \n\n{input3}")
        self.status.setText("Отправлено!")


     

       
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()