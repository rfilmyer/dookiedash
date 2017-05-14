import boto3

from email_text import plain_text_message_raw, html_message_raw

ses = boto3.client('ses')

from_email = "dookiedashdelivery@gmail.com"

def format_email(order_id="A1B2C3",
                 address="1600 Pennsylvania Avenue NW\nWashington, DC 20500",
                 bitcoin_amt="0.0095",
                 wallet_id="a1b2c3d4e5f60123456789"):
    return (plain_text_message_raw.format(order_id=order_id,
                                          address=address,
                                          bitcoin_amt=bitcoin_amt,
                                          wallet_id=wallet_id),
            html_message_raw.format(order_id=order_id,
                                    address=address.replace('\n', '<br>'),
                                    bitcoin_amt=bitcoin_amt,
                                    wallet_id=wallet_id))

def send_email(plain_text_message, html_message, recipient=from_email):
    dest = {"ToAddresses": [recipient]}
    message = {"Subject": {"Data": "Hey! 🐎💩✉️ Your Order is on its Way!", "Charset": "utf-8"},
               "Body": {"Text": {"Data": plain_text_message, "Charset": "UTF-8"},
                        "Html": {"Charset": "UTF-8", "Data": html_message}}}
    response = ses.send_email(Source=from_email, Destination=dest, Message=message)
    return response

if __name__ == '__main__':
    plain_text_message, html_message = format_email()
    send_email(plain_text_message, html_message)