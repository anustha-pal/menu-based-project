Menu Based Program:


from twilio.rest import Client
import pywhatkit
import smtplib
import schedule
import time
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
from googlesearch import search

print("Welcome to our App")

print("""
press 1: send WhatsApp
press 2: send SMS
press 3: call someone
press 4: mail someone
press 5: scrape top 5 results
press 6: schedule an email
""")

ch = input("Enter your choice: ")

if int(ch) == 1:
    user_num = input("Enter the number to whom you want to send a message (in format +<country code><number>): ")
    msg = input("Enter your message here: ")
    time_hr = int(input("Enter time in hour (24-hour format): "))
    time_min = int(input("Enter time in minute: "))
    pywhatkit.sendwhatmsg(user_num, msg, time_hr, time_min)
    print("Message sent successfully.....")

elif int(ch) == 2:
    account_sid = 'ACa93a2993c73c903de9baa1f6fc9c6997'
    auth_token = '82c2f24f1678ea7e3524206dfdca71d0'
    client = Client(account_sid, auth_token)

    twilio_phone_number = '+19788296616'
    recipient_phone_number = input("Enter recipient number (linked with Twilio): ")

    message = client.messages.create(
        body=input("Enter your text message: "),
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print(f"Message sent successfully. SID: {message.sid}")

elif int(ch) == 3:
    account_sid = 'ACa93a2993c73c903de9baa1f6fc9c6997'
    auth_token = '82c2f24f1678ea7e3524206dfdca71d0'
    client = Client(account_sid, auth_token)

    twilio_phone_number = '+19788296616'
    recipient_num = input("Enter number to call (in format +<country code><number>): ")

    twiml_url = 'http://demo.twilio.com/docs/voice.xml'

    call = client.calls.create(
        to=recipient_num,
        from_=twilio_phone_number,
        url=twiml_url
    )

    print(f"Call is going on.....Call SID: {call.sid}")

elif int(ch) == 4:
    def send_email(sender_email, receiver_email, password, subject, body):
        message = MIMEText(body)
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

    sender_email = "sachinkumar@gmail.com"
    receiver_email = input("Enter receiver Mail ID: ")
    password = "zyce vayi zjdk izww"
    subject = input("Enter subject of Mail: ")
    body = input("Enter body of Mail: ")

    send_email(sender_email, receiver_email, password, subject, body)

elif int(ch) == 5:
    def scrape_top_5_results(query):
        search_results = search(query, num_results=3)
        results_data = []

        for url in search_results:
            try:
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, 'html.parser')
                title = soup.title.string if soup.title else 'No title'
                meta_desc = soup.find('meta', attrs={'name': 'description'})
                description = meta_desc['content'] if meta_desc else 'No description'

                results_data.append({
                    'url': url,
                    'title': title,
                    'description': description
                })
            except Exception as e:
                print(f"Failed to scrape {url}: {e}")

        return results_data

    query = input("Enter your query: ")
    results = scrape_top_5_results(query)

    for idx, result in enumerate(results, start=1):
        print(f"Result {idx}:")
        print(f"URL: {result['url']}")
        print(f"Title: {result['title']}")
        print(f"Description: {result['description']}")
        print("-" * 80)

elif int(ch) == 6:
    def send_email(sender_email, receiver_email, password, subject, body):
        message = MIMEText(body)
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

    def schedule_email(sender_email, receiver_email, password, subject, body, send_time):
        schedule.every().day.at(send_time).do(send_email, sender_email, receiver_email, password, subject, body)
        while True:
            schedule.run_pending()
            time.sleep(1)

    sender_email = "anusthapal@gmail.com"
    receiver_email = input("Enter receiver email: ")
    password = "zyce vayi zjdk izww"
    subject = input("Enter subject of email: ")
    body = input("Enter body of email: ")
    send_time = input("Enter time to send email (HH:MM format): ")

    schedule_email(sender_email, receiver_email, password, subject, body, send_time)

else:
    print("Invalid choice, please try again.")








