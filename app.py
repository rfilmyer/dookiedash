from aiohttp import web

from notifications import format_email, send_email
from order_form import create_shitexpress_order

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, {name}"
    return web.Response(text=text.format(name=name))

async def email(request):
    order_details = create_shitexpress_order()
    plain_text_message, html_message = format_email(order_id=order_details['order_id'],
                                                    address=order_details['address'],
                                                    bitcoin_amt=order_details['amount'],
                                                    wallet_id=order_details['btc_address'])
    email_response = send_email(plain_text_message, html_message)
    return web.json_response(email_response)

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/email', email)
app.router.add_post('/email', email)

web.run_app(app, host='localhost', port=8000)