import smtplib
import ssl


def send_email(message):  #
    host = 'smtp.gmail.com'
    port = 465

    username = 'alanshenjc@gmail.com'
    password = 'nuqu zbal aley pxnb'  # app password

    receiver = 'alanshenjc@gmail.com'
    context = ssl.create_default_context()
    # slash here to make sure it doesn't think we have a break lines here

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
