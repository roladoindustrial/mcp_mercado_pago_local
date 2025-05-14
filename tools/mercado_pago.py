import requests
import os
from mcp_sdk.tool import tool

@tool(name="crear_pago_mp", description="Genera un link de pago en Mercado Pago")
def crear_pago_mp(cliente: str, descripcion: str, monto: float) -> dict:
    access_token = os.getenv("MP_ACCESS_TOKEN")
    url = "https://api.mercadopago.com/checkout/preferences"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    body = {
        "items": [{
            "title": descripcion,
            "quantity": 1,
            "currency_id": "MXN",
            "unit_price": monto
        }],
        "payer": {"name": cliente},
        "back_urls": {
            "success": "https://tuservidor.com/success",
            "failure": "https://tuservidor.com/failure",
            "pending": "https://tuservidor.com/pending"
        },
        "notification_url": "https://tu-mcp-railway.up.railway.app/webhook"
    }

    res = requests.post(url, headers=headers, json=body)
    return res.json()
