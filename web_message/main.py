import json
import re

import redis
from fastapi import FastAPI, Request, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

#app.mount("/static", StaticFiles(directory="static"), name="static")

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    chat_id = "default_chat"
    
    messages = [json.loads(msg) for msg in r.lrange(chat_id, 0, -1)]
    
    if not messages:
        welcome_message = {
            "text": "Bem-vindo ao chat de dúvidas! Por favor, escolha uma das opções:\n1: Aluno\n2: Instrutor"
        }
        r.lpush(chat_id, json.dumps(welcome_message))
        messages.insert(0, welcome_message)
    
    await websocket.send_text(json.dumps({"messages": messages}))
    
    while True:
        data = await websocket.receive_text()
        message = json.loads(data)
        
        if message.get("text") == "1":
            response = "Deixe seu e-mail para entrarmos em contato e tirarmos suas dúvidas em relação aos nossos cursos!!"
        elif message.get("text") == "2":
            response = "Deixe seu e-mail para entrarmos em contato e tirarmos suas dúvidas em relação a como cadastrar seus cursos."
        elif re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", message.get("text")):
            response = f"O e-mail {message.get('text')} foi validado. Entraremos em contato em breve!"
        else:
            response = "E-mail inválido. Por favor, digite um e-mail válido."
        
        r.lpush(chat_id, json.dumps(message))
        
        if response:
            response_message = {"text": response}
            r.lpush(chat_id, json.dumps(response_message))
            await websocket.send_text(json.dumps(response_message))
        
        await websocket.send_text(json.dumps(message))

