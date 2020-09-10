from typing import List, Optional
from pydantic import BaseModel


class BaseRequest(BaseModel):
    title: str
    body: str

class Notifier(BaseModel):
    name: str
    payload: Optional[dict] = {}

class NotifyRequest(BaseRequest):
    notifiers: List[Notifier]


class TelegramRequest(BaseRequest):
    chat_id: str