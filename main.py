from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.uic import loadUi

import smtplib
import config
import sys

class Form(QMainWindow):
    def __init__(self):
            super(Form, self).__init__()


            loadUi('mailing.ui',self)
            self.send_button.clicked.connect(self.button_send)


    def button_send(self):
        try:
            gmail = str(self.gmail.text())
            theme = str(self.theme.text())
            message = str(self.message.text())
            sender = config.sender
            password =config.password

    
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender,password)
            server.sendmail(sender, gmail,  f'Subject: {theme}  \n\n {message}')
            self.loading.setText("Рассылка отправлена! ")


        except :
                self.loading.setText("Произошла ошибка, повторите попытку!")



app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()