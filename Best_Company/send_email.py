import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "suryaprakashsharma453@gmail.com"
    password = "sdum bzor liuv rzny"

    receiver_email = "suryaprakashsharma453@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)

