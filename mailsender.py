import smtplib 



mails = {"name1":"name1-email@example.com",
    "name2":"name2-email@example.com"
    
}



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@example.com', 'your-passward')
    server.sendmail('yourmail@example.com', to, content)
    server.close()


try:

    #takes input from user and checks whom to send mail from dictionary provided above
    re=input("whom to send:\t")
    
    to = mails[re] 

    content=input("What should I say: \t")
    
    sendEmail(to, content)
    print(f"reciever{to}")
    print(f"message{content}")

    print("Email has been sent!")
except Exception as e:
    print(e)
    print("not able to send email..check wheather the reciever is there on list...")
