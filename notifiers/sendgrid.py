from typing import Optional
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Content

from notifiers.notifier import Notifier
from config import SENDGRID_API_KEY, SENDGRID_FROM_ADDRESS


class Sendgrid(Notifier):
    async def notify(self, title: str, body: str, to_addr: str, from_addr: Optional[str] = None):
        try:
            message = Mail(
                from_email=SENDGRID_FROM_ADDRESS if from_addr is None else from_addr, 
                to_emails=to_addr, 
                subject=title, 
                plain_text_content=body)
            response = SendGridAPIClient(SENDGRID_API_KEY).send(message)
            if not response.status_code < 300:
                return {'name': 'sendgrid', 'status': 'error', 'message': f"Email send failed: {response.status_code}"}
        except Exception as e:
            return {'name': 'sendgrid', 'status': 'error', 'message': repr(e)}
        return {'name': 'sendgrid', 'status': 'ok'}