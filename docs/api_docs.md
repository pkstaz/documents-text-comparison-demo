# 🚀 Documentación API

## Endpoints Principales

### POST /chat
Enviar mensaje al chatbot

```json
{
  "session_id": "user123",
  "message": "Hola",
  "files": []
}
```

### POST /upload
Subir archivos PDF

### GET /session/{id}
Obtener estado de sesión

### DELETE /session/{id}
Eliminar sesión

## Ejemplos de Uso

### Python
```python
import requests

response = requests.post("http://localhost:8000/chat", json={
    "session_id": "user123",
    "message": "comparar pdfs"
})
```

### cURL
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"session_id": "user123", "message": "hola"}'
```
