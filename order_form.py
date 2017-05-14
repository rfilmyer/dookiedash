import requests

form_sample_data = {
    "btc": 1,
    "email": "dookiedashdelivery@gmail.com",
    "name": "Donald J. Trump",
    "street": "1600 Pennsylvania Avenue NW",
    "city": "Washington",
    "zip": "20500",
    "state": "DC",
    "country": "US",
    "notes": "",
    "animal": "horse",
    "packaging": 1,
    "custom": "",
    "referer": ""
}
form_url = "http://en.shitexpress.com/btc/create.php"


def parse_shitexpress_response(text: str):
    parameters = text.split('|')
    return {"order_id": parameters[0],
            "btc_address": parameters[2],
            "amount": parameters[3]}

def create_shitexpress_order():
    response = requests.post(form_url, data=form_sample_data)
    complete_order = parse_shitexpress_response(response.text)
    complete_order["address"] = "{street}\n{city}, {state} {zip}".format(street=form_sample_data['street'],
                                                                         city=form_sample_data['city'],
                                                                         state=form_sample_data['state'],
                                                                         zip=form_sample_data['zip'])
    return complete_order

if __name__ == '__main__':
    print(create_shitexpress_order())
