import httpx

from notifiers.notifier import Notifier
from config import SERVER_CHAN_SCKEY


class ServerChan(Notifier):
    async def notify(self, title: str, body: str):
        try:
            url = 'https://sc.ftqq.com/{}.send?text={}&desp={}'.format(SERVER_CHAN_SCKEY, title, body)
            async with httpx.AsyncClient() as client:
                resp = await client.get(url)
                if not resp.status_code < 300:
                    return {'name': 'server_chan', 'status': 'error', 'message': f"Server chan send failed: {resp.status_code}"}
        except Exception as e:
            return {'name': 'server_chan', 'status': 'error', 'message': repr(e)}
        return {'name': 'server_chan', 'status': 'ok'}