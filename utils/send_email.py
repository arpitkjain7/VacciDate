import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import json
from datetime import datetime


def send_email(receiver_email, appointment_details, user_name):
    sender_email = "email"
    password = "password"
    message = MIMEMultipart("alternative")
    message["Subject"] = "Vaccine slot available"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    Please find below vaccine slot availablity for you,
    slot available at 4:00 PM 06/05/2021 at Jahangir Hospital, Pune
    click here to navigate to the hostpital"""
    html = f"""\
    <html>
    <body>
        <p>Hi {user_name},<br>
        Please find below vaccine slot availablity for you,<br>

        {appointment_details.to_html()}<br>
        <a href="https://www.cowin.gov.in/home">Click here to book the appointment</a>
        </p>
        <p>Please reply back to us on this email if you dont want to receive the updates anymore.</p>
        <p>Regards,<br>
        Team Dobby<br>
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    return True


def send_email_wrapper(receiver_email: str, appointment_details: str, name: str):
    try:
        df_appointment = pd.DataFrame(appointment_details)
        date_format = "%Y-%m-%d %H:%M:%S"
        today_date = datetime.today()
        today_date = today_date.strftime(date_format)
        today_date = datetime.strptime(today_date, date_format)
        print(today_date)
        with open("data/mail_sent_data.json", "r") as f:
            data = json.load(f)
        date = data.get(receiver_email, None)
        if date is not None:
            delta = today_date - datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            if delta.total_seconds() >= 3600:
                send_email(receiver_email, df_appointment, name)
                data.update({receiver_email: str(today_date)})
        else:
            send_email(receiver_email, df_appointment, name)
            data.update({receiver_email: str(today_date)})
        with open("data/mail_sent_data.json", "w") as f:
            json.dump(data, f)
        return True
    except Exception:
        return False
