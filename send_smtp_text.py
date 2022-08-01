import os
import smtplib  # модуль smtp
import re  # regex
from email.mime.text import MIMEText  # модуль для кириллицы

regex = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def isValid(recepient_email):
    """ Валидация email """

    if re.fullmatch(regex, recepient_email):
        return True
    else:
        print("Неверный формат, повторите снова.\n")
        return False


def send_email(recipient, subject, message):
    """ Отправка почты """

    sender = "YOUR_EMAIL"
    password = os.getenv("GMAIL_APP_PASS")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = subject
        server.sendmail(sender, recipient, msg.as_string())

        return "Сообщение успешно отправлено!"
    except Exception as _ex:
        return f"{_ex}\nНеверный логин или пароль Gmail!"


def main():
    while True:
        recipient = input("Введите email получателя: ")
        if isValid(recipient) == True:
            break
    subject = input("Введите заголовок: ")
    message = input("Введите сообщение: ")
    print(send_email(recipient=recipient, subject=subject, message=message))


if __name__ == "__main__":
    main()
