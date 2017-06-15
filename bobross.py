import plugins
import urllib.request

def _initialise(bot):
    plugins.register_user_command(["bobross"])

def bobross(bot, event, *args):
    """random bob ross quote"""

    url = 'http://www.bobrossquotes.com/text.php'
    resp = urllib.request.urlopen(url).read()
    data = resp.decode('utf-8')

    yield from bot.coro_send_message(event.conv, _("<i>{}</i>").format(data))
