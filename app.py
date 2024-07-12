from aiohttp import web, ClientSession
import config
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%y-%m-%d %H:%M:%S', level=logging.DEBUG)

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello world")

@routes.post('/notification')
async def harmony_notification(request):
    try:
        logging.info("Request received")
        dataRequest = await request.json()
        # logging.info(dataRequest)
        cluster_name = dataRequest['cluster_name']
        tenant_name = dataRequest['tenant_name']
        alert_name = dataRequest['alert_name']
        timestamp = dataRequest['timestamp']
        text = dataRequest['text']
        severity_string = dataRequest['severity_string']
        trig_display_name = dataRequest['trig_display_name']
        url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
        headers = {
            "method": "POST",
            "contentType": "applicaton/json"
        }
        data = {
            'chat_id': config.TELEGRAM_CHAT_ID,
            'parse_mode': 'HTML',
            'text': f"<b>{severity_string}: {alert_name}</b>\n\n<b>Timestamp:</b> {timestamp}\n<b>Cluster:</b> {cluster_name}\n<b>Tenant:</b> {tenant_name}\n<b>Trigger:</b> {trig_display_name}\n\n<b>Message:</b> <i>{text}</i>"
        }

        logging.info("Begin sending message to Telegram bot")        
        async with ClientSession() as session:
            async with session.post(url=url, headers=headers, json=data) as response:
                # responseData = await response.json()
                logging.info("Message sent")
        
        return web.HTTPOk()

    except Exception as ex:
        logging.error(ex)

try:
    port = config.PORT
except:
    port = 8080

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=port)