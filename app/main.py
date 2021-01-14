import logging

from aiohttp import web

logging.basicConfig(format='[%(asctime)s.%(msecs)03d] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %I:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


async def index(request):
    logging.info('entrypoint in index endpoint')

    return web.Response(text="Welcome home!")


web_app = web.Application()
web_app.router.add_get('/', index)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    web.run_app(web_app)
