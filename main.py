@app.post("/webhook")
async def mercado_pago_webhook(request: Request):
    body = await request.json()
    print("🔔 Webhook recibido:", body)
    return {"status": "ok"}
