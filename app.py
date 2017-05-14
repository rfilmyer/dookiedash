import json

from aiohttp import web

from notifications import send_email


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, {name}"
    return web.Response(text=text.format(name=name))

async def email(request):
    email_response = send_email()
    return web.json_response(email_response)

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/email', email)
app.router.add_post('/email', email)
app.router.add_get('/{name}', handle)

web.run_app(app, host='localhost', port=8000)