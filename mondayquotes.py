import random
import smtplib
import datetime as dt

now=dt.datetime.now()
weekday=now.weekday()

my_email='datirsayali12@gmail.com'
my_pass='zztaxtrnssqmupuz'

quotes=["When you arise in the morning think of what a privilege it is to be alive, to think, to enjoy, to love...",
"Either you run the day or the day runs you.",
"Mondays are the start of the work week which offer new beginnings 52 times a year!",
"You've got to get up every morning with determination if you're going to go to bed with satisfaction.",
"Be miserable. Or motivate yourself. Whatever has to be done, it's always your choice.",
"Your Monday morning thoughts set the tone for your whole week. See yourself getting stronger, and living a fulfilling, happier & healthier life.",
"You don't have to be great to start, but you have to start to be great.",
"Each morning when I open my eyes I say to myself: I, not events, have the power to make me happy or unhappy today. I can choose which it shall be. Yesterday is dead, tomorrow hasn't arrived yet. I have just one day, today, and I'm going to be happy in it."]
print(weekday)
if weekday == 2:
    file=random.choice(quotes)
    print(file)
    connection=smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(my_email,my_pass)
    connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"monday motivation {file}")
