# 🤖 Comparador de PDFs con Chatbot IA

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-🔗-green.svg)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-🎈-red.svg)](https://streamlit.io)
[![FastAPI](https://img.shields.io/badge/FastAPI-🚀-teal.svg)](https://fastapi.tiangolo.com)

> **Sistema inteligente para comparar documentos PDF usando múltiples técnicas de IA y un chatbot conversacional.**

## 🌟 Características Principales

### 🔍 **Análisis Múltiple**
- **Análisis Básico** - Comparación línea por línea con difflib
- **Análisis Semántico** - Similitud conceptual con embeddings
- **Análisis TF-IDF** - Palabras clave y temas importantes
- **Análisis IA** - Comprensión contextual con LLMs (vLLM, OpenAI, Ollama)

### 🤖 **Chatbot Inteligente**
- **Estados conversacionales** - Manejo inteligente del flujo
- **Comandos especializados** - `/help`, `/status`, `/reset`
- **Análisis por dominio** - Legal, técnico, académico
- **Reportes automáticos** - Generación de informes detallados

### 🎨 **Múltiples Interfaces**
- **💬 Consola** - Chat simple en terminal
- **🌐 Streamlit** - Interfaz web moderna
- **🎨 Gradio** - UI visual e interactiva
- **🚀 FastAPI** - API REST para integraciones
- **📱 Telegram** - Bot nativo de Telegram
- **📞 WhatsApp** - Integración con Twilio

## 🚀 Instalación Rápida

### 1. Clonar e Instalar Dependencias

```bash
# Clonar repositorio
git clone <tu-repositorio>
cd pdf-comparator-chatbot

# Instalar dependencias básicas
pip install PyPDF2 sentence-transformers scikit-learn nltk pandas numpy matplotlib seaborn

# Instalar LangChain
pip install langchain langchain-community langchain-openai

# Instalar interfaces web (opcional)
pip install streamlit gradio fastapi uvicorn

# Instalar integraciones mensajería (opcional)
pip install python-telegram-bot twilio

# Instalar vLLM para modelos locales (opcional)
pip install vllm
```

### 2. Configuración Básica

```python
# Configurar rutas de PDFs
PDF1_PATH = "documentos/documento1.pdf"
PDF2_PATH = "documentos/documento2.pdf"

# Configurar proveedor LLM
LLM_PROVIDER = "vllm"  # Opciones: "vllm", "openai", "ollama"
```

## 🎯 Uso Rápido

### 🖥️ **Chatbot de Consola**
```python
# Ejecutar chat simple
ejecutar_chatbot_consola()
```

### 🌐 **Interfaz Web Streamlit**
```bash
# En terminal
streamlit run app.py
```

### 🎨 **Interfaz Gradio**
```python
# Ejecutar interfaz visual
demo = crear_interfaz_gradio()
demo.launch(share=True)
```

### 🚀 **API REST**
```python
# Iniciar servidor FastAPI
ejecutar_fastapi_server()
# Acceder a: http://localhost:8000/docs
```

## 🤖 Configuración de LLMs

### **vLLM (Local)**
```bash
# Instalar vLLM
pip install vllm

# Ejecutar servidor
python -m vllm.entrypoints.openai.api_server \
  --model meta-llama/Llama-2-7b-chat-hf \
  --host localhost \
  --port 8000
```

### **OpenAI**
```python
# Configurar API key
OPENAI_CONFIG = {
    "api_key": "tu_openai_api_key",
    "model": "gpt-3.5-turbo"
}
```

### **Ollama (Local)**
```bash
# Instalar Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Ejecutar servidor
ollama serve

# Descargar modelo
ollama pull llama2
```

## 📋 Guía de Uso del Chatbot

### **Comandos Básicos**
- `/start` - Iniciar nueva comparación
- `/help` - Mostrar ayuda completa
- `/status` - Ver estado actual
- `/reset` - Reiniciar sesión

### **Flujo Típico de Conversación**

```
👤 Usuario: "Hola"
🤖 Bot: "¡Hola! Soy tu asistente para comparar PDFs..."

👤 Usuario: "Comparar documentos"
🤖 Bot: "Perfecto! Envía el primer PDF..."

👤 Usuario: [sube archivo.pdf]
🤖 Bot: "✅ Primer PDF recibido. Envía el segundo..."

👤 Usuario: [sube archivo2.pdf] 
🤖 Bot: "¿Qué análisis quieres? 1️⃣Rápido 2️⃣Completo 3️⃣Legal..."

👤 Usuario: "completo"
🤖 Bot: "🎉 Análisis completado! Similitud: 78.5%..."

👤 Usuario: "reporte"
🤖 Bot: "📊 REPORTE DETALLADO DE COMPARACIÓN..."
```

### **Comandos Post-Análisis**
- `reporte` - Generar reporte completo
- `exportar` - Descargar resultados
- `nuevo` - Nueva comparación
- `analisis` - Ver detalles por método
- `resumen` - Resumen ejecutivo

## 🎯 Tipos de Análisis

### **1. Análisis Rápido**
- Resumen básico (2-3 minutos)
- Puntuación general de similitud
- Principales similitudes y diferencias

### **2. Análisis Completo** 
- Análisis detallado (5-10 minutos)
- Múltiples métodos de comparación
- Reportes visuales y gráficos

### **3. Análisis Especializado**
- **Legal** - Contratos, normativas
- **Técnico** - Documentación, manuales
- **Académico** - Papers, artículos científicos

## 🔧 Configuración Avanzada

### **Manager Central**
```python
# Configurar todo el sistema
chatbot_manager.configurar(
    llm_provider="openai",
    telegram_token="tu_token",
    openai_api_key="tu_key"
)

# Usar cualquier interfaz
bot_consola = chatbot_manager.crear_chatbot_consola()
bot_telegram = chatbot_manager.crear_chatbot_telegram()
```

### **Templates Personalizados**
```python
# Modificar prompts existentes
prompt_templates["comprehensive"].template = "Tu prompt personalizado..."

# Crear template específico
template_personalizado = PromptTemplate(
    input_variables=["documento1", "documento2"],
    template="Analiza desde perspectiva de: {perspectiva}..."
)
```

## 📱 Integraciones de Mensajería

### **Telegram Bot**
```python
# Configurar bot
TOKEN = "tu_token_de_telegram"
bot = configurar_telegram_bot(TOKEN)
bot.ejecutar_bot()
```

### **WhatsApp (Twilio)**
```python
# Configurar webhook
whatsapp_bot = WhatsAppChatbot(
    account_sid="tu_sid",
    auth_token="tu_token",
    whatsapp_number="+1234567890"
)
```

## 🌐 API REST Endpoints

### **Endpoints Principales**
- `POST /chat` - Enviar mensaje al chatbot
- `POST /upload` - Subir archivos PDF
- `GET /session/{id}` - Estado de sesión
- `DELETE /session/{id}` - Eliminar sesión

### **Ejemplo de Uso API**
```python
import requests

# Enviar mensaje
response = requests.post("http://localhost:8000/chat", json={
    "session_id": "user123",
    "message": "hola"
})

# Subir archivos
files = {'files': open('documento.pdf', 'rb')}
response = requests.post("http://localhost:8000/upload", 
                        data={"session_id": "user123"}, 
                        files=files)
```

## 📊 Estructura del Proyecto

```
📁 Proyecto/
├── 📄 README.md
├── 📄 requirements.txt
├── 📁 notebooks/
│   ├── 📓 comparador_pdf_langchain.ipynb
│   └── 📓 chatbot_pdf_comparator.ipynb
├── 📁 src/
│   ├── 🐍 pdf_comparator.py
│   ├── 🤖 chatbot_core.py
│   ├── 🌐 streamlit_app.py
│   ├── 🎨 gradio_app.py
│   └── 🚀 fastapi_app.py
├── 📁 docs/
│   ├── 📄 user_guide.md
│   └── 📄 api_docs.md
└── 📁 examples/
    ├── 📄 documento1.pdf
    └── 📄 documento2.pdf
```

## 🎮 Ejemplos de Uso

### **Comparación Legal**
```python
# Análisis especializado en documentos legales
resultados = analisis_por_dominio("documentos legales y contratos")
```

### **Análisis por Lotes**
```python
documentos = [
    ("contrato1.pdf", "contrato2.pdf"),
    ("manual1.pdf", "manual2.pdf"),
    ("paper1.pdf", "paper2.pdf")
]

for pdf1, pdf2 in documentos:
    resultado = comparar_pdfs_completo(pdf1, pdf2)
    print(f"Similitud: {resultado['puntuacion_similitud_combinada']:.2%}")
```

### **Exportación de Resultados**
```python
# Generar reporte
reporte = generar_reporte_texto(resultados)

# Exportar a JSON
exportar_resultados(resultados, "analisis_2024.json")

# Obtener estadísticas
stats = obtener_estadisticas_comparacion(resultados)
```

## 🔍 Debugging y Troubleshooting

### **Verificar Sistema**
```python
# Verificar estado completo
verificar_estado_sistema()

# Probar conexión LLM
probar_conexion_llm()

# Cambiar proveedor si hay problemas
cambiar_proveedor_llm("ollama")
```

### **Problemas Comunes**

#### **Error NLTK punkt_tab**
```python
import nltk
nltk.download('punkt_tab')
```

#### **vLLM no conecta**
```bash
# Verificar que el servidor esté corriendo
curl http://localhost:8000/health
```

#### **Archivos PDF no se leen**
```python
# Verificar rutas
print(f"Existe PDF1: {os.path.exists(PDF1_PATH)}")
print(f"Existe PDF2: {os.path.exists(PDF2_PATH)}")
```

## 🎯 Modelos Recomendados

### **vLLM (Local)**
- `meta-llama/Llama-2-7b-chat-hf` - General
- `mistralai/Mistral-7B-Instruct-v0.1` - Rápido
- `clibrain/lince-zero-spanish-7b` - Español

### **Ollama (Local)**
- `llama2`, `llama2:13b` - Propósito general
- `mistral:7b` - Eficiente
- `codellama:7b` - Código y técnico

### **OpenAI (Cloud)**
- `gpt-3.5-turbo` - Económico y rápido
- `gpt-4` - Máxima calidad
- `gpt-4-turbo` - Balance calidad/velocidad

## 📈 Métricas y Análisis

### **Tipos de Similitud**
- **Textual** - Comparación exacta de caracteres
- **Semántica** - Similitud de significado
- **Temática** - Temas y palabras clave comunes
- **Contextual** - Comprensión profunda con IA

### **Interpretación de Puntuaciones**
- **90-100%** - Documentos prácticamente idénticos
- **80-89%** - Muy similares, diferencias menores
- **70-79%** - Similares con diferencias notables
- **60-69%** - Similitudes moderadas
- **40-59%** - Algunas similitudes
- **20-39%** - Pocas similitudes
- **0-19%** - Muy diferentes

## 🤝 Contribuciones

### **Cómo Contribuir**
1. Fork del repositorio
2. Crear branch feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push al branch (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

### **Áreas de Mejora**
- ✨ Nuevos tipos de análisis especializados
- 🌍 Soporte para más idiomas
- 📊 Visualizaciones avanzadas
- 🔧 Optimizaciones de rendimiento
- 📱 Más integraciones de mensajería

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

## 🆘 Soporte

### **Documentación**
- 📖 [Guía de Usuario](docs/user_guide.md)
- 🔧 [Documentación API](docs/api_docs.md)
- 🎥 [Videos Tutoriales](https://youtube.com/playlist)

### **Comunidad**
- 💬 [Discord](https://discord.gg/tu-servidor)
- 🐦 [Twitter](https://twitter.com/tu-cuenta)
- 📧 [Email](mailto:soporte@tu-proyecto.com)

### **Reportar Bugs**
1. Crear issue en GitHub
2. Incluir pasos para reproducir
3. Adjuntar logs de error
4. Especificar versión de Python y OS

---

## 🏆 Créditos

**Desarrollado con ❤️ usando:**
- [LangChain](https://langchain.com) - Framework de IA
- [Streamlit](https://streamlit.io) - Interfaz web
- [Gradio](https://gradio.app) - UI interactiva
- [FastAPI](https://fastapi.tiangolo.com) - API REST
- [sentence-transformers](https://huggingface.co/sentence-transformers) - Embeddings
- [vLLM](https://vllm.ai) - Inferencia local de LLMs

**Agradecimientos especiales a la comunidad open source** 🙏

---

<div align="center">

### 🚀 ¡Comienza a comparar PDFs con IA ahora!

[📖 Documentación](docs/) | [🎮 Demo en Vivo](https://demo.tu-proyecto.com) | [💬 Discord](https://discord.gg/tu-servidor)

**¿Te gusta el proyecto? ⭐ Dale una estrella en GitHub**

</div>