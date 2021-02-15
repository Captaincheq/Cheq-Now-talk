import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('alecmabhizachirawu@gmail.com', 'Chirawu123412')
server.sendmail('fresh.grandma21@gmail.com', 'alecmabhizachirawu@outlook.com', ' Make sure you learn my friend')
