import httpx
from typing import Optional, Dict

from notifiers.notifier import Notifier
from config import PUSHBULLET_ACCESS_TOKEN


class Pushbullet(Notifier):
    async def notify(self, title: str, body: str, url: Optional[str] = None, device_iden: Optional[str] = None):
        try:
            data = {
                'title': title, 
                'body': body, 
                'type': 'note'}

            if url is not None:
                data['type'] = 'link'
                data['url'] = url
            if device_iden is not None:
                data['device_iden'] = device_iden
            headers = {'Access-Token': PUSHBULLET_ACCESS_TOKEN}
            async with httpx.AsyncClient() as client:
                resp = await client.post('https://api.pushbullet.com/v2/pushes', data=data, headers=headers)
                if not resp.status_code < 300:
                    return {
                        'name': 'pushbullet', 
                        'status': 'error', 
                        'message': f"Pushbullet send failed[{resp.status_code}]: {resp.json()['error'].get('message')}"}
        except Exception as e:
            return {'name': 'pushbullet', 'status': 'error', 'message': repr(e)}
        return {'name': 'pushbullet', 'status': 'ok'}