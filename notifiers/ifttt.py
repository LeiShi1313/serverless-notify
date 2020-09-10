import httpx
from typing import Optional

from notifiers.notifier import Notifier
from config import IFTTT_KEY, IFTTT_EVENT


class Ifttt(Notifier):
    async def notify(self, title: str, body: str, url: Optional[str] = None, event: Optional[str] = None):
        try:
            ifttt_url = 'https://maker.ifttt.com/trigger/{}/with/key/{}'.format(
                IFTTT_EVENT if event is None else event, IFTTT_KEY)
            data = {'value1': title, 'value2': body}
            if url is not None:
                data['value3'] = url
            async with httpx.AsyncClient() as client:
                resp = await client.post(ifttt_url, data=data)
                if not resp.status_code < 300:
                    return {
                        'name': 'ifttt', 
                        'status': 'error', 
                        'message': f"IFTTT send failed[{resp.status_code}]: {resp.json()['errors']}"}
        except Exception as e:
            return {'name': 'ifttt', 'status': 'error', 'message': repr(e)}
        return {'name': 'ifttt', 'status': 'ok'}
