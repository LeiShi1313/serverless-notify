import os

# Sendgrid
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', '')
SENDGRID_FROM_ADDRESS = os.environ.get('SENDGRID_FROM_ADDRESS', 'notifier@leishi.io')

# IFTTT
IFTTT_EVENT = os.environ.get('IFTTT_EVENT', '')
IFTTT_KEY = os.environ.get('IFTTT_KEY', '')

# Pushbullet
PUSHBULLET_ACCESS_TOKEN = os.environ.get('PUSHBULLET_ACCESS_TOKEN', '')

# Telegram
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '')

# Server Chan
SERVER_CHAN_SCKEY = os.environ.get('SERVER_CHAN_SCKEY', '')