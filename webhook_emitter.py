import requests

# URL del webhook receptor
webhook_url = "http://localhost:5000/webhook"

# Datos simulados del evento
data = {
    "user_id": 123,
    "name": "John Doe",
    "email": "john.doe@example.com"
}

# Enviar datos al webhook
response = requests.post(webhook_url, json=data)

print(f"Webhook sent, server response: {response.status_code}")
