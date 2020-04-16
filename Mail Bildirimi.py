import smtplib
from email.mime.text \
import MIMEText
 
smtpadresi = "smtp.gmail.com"
##sabit kalacak
smtpport = 587
kullaniciadi = "asdfg@gmail.com"
##kendi mail adresiniz
sifre = "şifreburaya"
##kendi mailinizin şifresi
 
gonderilecekadres = ["asdfg@gmail.com]
##ileinin gönderileceği mail adresi
konu = "Bilgisayar Açıldı"
icerik = """
 
Bilgisayar Açıldı

"""
 
mail = MIMEText(icerik, "html", "utf-8")
mail["From"] = kullaniciadi
mail["Subject"] = konu
mail["To"] = ",".join(gonderilecekadres)
 
mail = mail.as_string()
 

 
s = smtplib.SMTP(smtpadresi,smtpport)
s.starttls()
s.login(kullaniciadi, sifre)
s.sendmail(kullaniciadi, gonderilecekadres, mail)

