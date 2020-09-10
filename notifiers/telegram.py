import httpx
from typing import Optional, Dict

from notifiers.notifier import Notifier
from config import TELEGRAM_BOT_TOKEN


class Telegram(Notifier):
    async def notify(self, title: str, body: str, chat_id: str):
        try:
            url = "https://api.telegram.org/bot{}/sendMessage?parse_mode=MarkdownV2&chat_id={}&text={}".format(
                TELEGRAM_BOT_TOKEN, chat_id,
                "*{}*\n\n{}".format(title, body))
            async with httpx.AsyncClient() as client:
                resp = await client.get(url)
                if not resp.status_code < 300:
                    return {
                        'name': 'telegram', 
                        'status': 'error', 
                        'message': f"Telegram send failed[{resp.status_code}]: {resp.json()['description']}"}
            return {'name': 'telegram', 'status': 'ok'}
        except Exception as e:
            return {'name': 'telegram', 'status': 'error', 'message': repr(e)}