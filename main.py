from fastapi import FastAPI, Request
from mcp_sdk.fastapi import serve_mcp
from tools.mercado_pago import crear_pago_mp

app = FastAPI()

# Servir las tools de MCP
serve_mcp(app, tools=[crear_pago_mp])

# Webhook para Mercado Pago
@app.post("/webhook")
async def mercado_pago_webhook(request: Request):
    body = await request.json()
    print("🔔 Webhook recibido:", body)
    return {"status": "ok"}
