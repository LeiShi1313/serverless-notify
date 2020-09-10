import uvicorn
import traceback
from typing import List
from mangum import Mangum
from pydantic import BaseModel
from starlette.requests import Request
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

from models import NotifyRequest
from notifiers import Notifier, router


app = FastAPI()
app.include_router(router)


@app.post("/notify")
async def notify(request: NotifyRequest):
    resps = []
    for notifier in request.notifiers:
        try:
            resp = await Notifier.notifiers[notifier.name].notify(
                request.title,
                request.body,
                **notifier.payload)
            resps.append(resp)
        except Exception as e:
            resps.append({
                'name': notifier.name,
                'status': 'error',
                'message': repr(e)
            })
    return resps


handler = Mangum(app, enable_lifespan=False)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')