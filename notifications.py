import boto3

ses = boto3.client('ses')

from_email = "roger.filmyer@gmail.com"

def send_email(recipient=from_email):
    dest = {"ToAddresses": [recipient]}
    message = {"Subject": {"Data": "Test 🐎💩✉️ Email", "Charset": "utf-8"},
               "Body": {"Text": {"Data": "This is a test email. 💩. That was an emoji.", "Charset": "utf-8"}}}
    response = ses.send_email(Source=from_email, Destination=dest, Message=message)
    return response


if __name__ == '__main__':
    send_email()