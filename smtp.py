import smtplib

sender = "adithyan18fm@gmail.com"
password = input(str("enter your password :"))
receiver = "adithyanfm@gmail.com"
message = " i love"

server = smtplib.SMTP("smtp.@gmail.com",587)
server.starttls()
server.login(sender,password)
print("login successful")
server.sendmail(sender,message)
print("message has succesfully send")
