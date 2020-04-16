"""
bekirarkali.blogspot.com
ig: @bekrarkali
github: https://github.com/ebubekir07/projeler
https://www.youtube.com/channel/UCfRC3PPhSJDlqjU_me437KA


Yazılımın çalışabilmesi için yazılımda gerekli ayarlar yapıldıktan sonra google
güvenliğinden "DAHA AZ GÜVENLİ UYGULAMA ERİŞİMİ" seçeneğini aktif hale
getirmeniz gerekiyor. Bu yazılımı uzun süre kullanmadığınız zaman google
ayarları eski hale getirecektir.

Windows'un zaman görevleyici uygulamasına bu yazılımın python kodunu ekleyerek
her bilgisayar açıldığında bu yazılımı çalıştırmasını sağlayabilirsiniz.
Böylece bilgisayar açılır açılmaz internet bağlantısı varsa size mail gelir ve
bilgisayarın açıldığından haberiniz olur.

Eğer isterseniz maili kendinize de gönderebilirsiniz.
Kodlar bana ait değildir. 
"""


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

