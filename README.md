# serverless-notify

A [FastApi](https://fastapi.tiangolo.com/) project integrated with [serverless](https://www.serverless.com/), with auto-generated interfaces that you can easily send notifications to multiple endpoints. Currently integrated with:
- [Sendgrid](https://sendgrid.com)
- [IFTTT Webhook](https://ifttt.com/maker_webhooks)
- [Pushbullet](https://docs.pushbullet.com/#push)
- [Telegram](https://core.telegram.org/bots)
- [Server Chan](http://sc.ftqq.com/)

## How to start locally

```shell
git clone https://github.com/LeiShi1313/serverless-notify.git
cd serverless-notify
npm install
pip install -r requirements.txt
uvicorn app:app --reload
```

and then open http://localhost:8000/docs to see auto-generated API docs and play with it!

## How to deploy to AWS Lambda

```shell
export SENDGRID_API_KEY=XXXXXXX
export IFTTT_KEY=XXXXXXXX
export PUSHBULLET_ACCESS_TOKEN=XXXXXXXXXXXXX
export SERVER_CHAN_SCKEY=XXXXXXXXXXXX
export TELEGRAM_BOT_TOKEN=XXXXXXXXXXXXX
sls deploy
```
