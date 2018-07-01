#!/usr/local/bin/python
#-*- coding: utf-8 -*-

# Connection widh database(mysql)
# Created: 2013/12/22

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# This is factory for mail
class MailFactory:

    # init
    def __init__(self,host=""):
        try:
            self.mailer = smtplib.SMTP(host)
            self.mail_from = ""
            self.tos = []
            self.subject = ""
            self.body = ""
            self.origin_encode = "utf-8"
            self.mail_encode = "iso-2022-jp"
        except:
            raise

# Setting for mail
class SendMail(MailFactory):

    def set_from(self, addr):
        self.mail_from = addr

    def set_tos(self, addr):
        self.tos.append(addr)

    def set_subject(self, subject):
        self.subject = subject

    def set_body(self, body):
        self.body = body.decode(self.origin_encode).encode(self.mail_encode)

    def make_message(self):
        m = MIMEText(self.body,'plain',self.mail_encode)
        m["subject"] = Header(self.subject)
        print m
        return m

    def send(self):
        message = self.make_message()
        self.mailer.sendmail(self.mail_from,self.tos,message.as_string())

if __name__ == '__main__':
    a = ("メールのテストをします。\n"
        "このメールが正しく受信すればOKです。 ¥n "
        "================="
        " \n\n\n  あなたの計画は明日実行することになっています"
        "*****************")
    s = SendMail("")
    s.set_from("")
    s.set_tos([""])
    s.set_subject("test_mail")
    s.set_body(a)
    s.send()
