@app.post("/webhook")
async def mercado_pago_webhook(request: Request):
    body = await request.json()

    payment_id = body.get("data", {}).get("id")
    if not payment_id:
        return {"error": "No payment ID in webhook"}

    # Consulta a Mercado Pago para confirmar estado real
    access_token = os.getenv("MP_ACCESS_TOKEN")
    url = f"https://api.mercadopago.com/v1/payments/{payment_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)

    payment_info = response.json()

    print("🧾 Detalles del pago:", payment_info)

    if payment_info.get("status") == "approved":
        # Aquí puedes llamar a Supabase o notificar a n8n
        print("✅ Pago aprobado")
    else:
        print("❌ Pago no aprobado aún")

    return {"status": "received"}
