#!/usr/bin/env python3
"""
Script para crear la estructura completa del repositorio
PDF Comparator with Chatbot AI

Uso: python setup_repository.py [nombre_proyecto]
"""

import os
import sys
from pathlib import Path
import json

def crear_estructura_repositorio(nombre_proyecto="pdf-comparator-chatbot"):
    """Crea la estructura completa del repositorio"""
    
    print(f"🚀 Creando estructura del repositorio: {nombre_proyecto}")
    print("=" * 60)
    
    # Crear directorio principal
    base_dir = Path(nombre_proyecto)
    base_dir.mkdir(exist_ok=True)
    
    # Estructura de directorios
    directorios = [
        "src",
        "notebooks", 
        "docs",
        "examples",
        "tests",
        "config",
        "data/pdfs",
        "data/results",
        "scripts",
        "assets/images",
        "assets/icons"
    ]
    
    # Crear directorios
    for directorio in directorios:
        dir_path = base_dir / directorio
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Creado: {directorio}/")
    
    # Crear archivos principales
    crear_archivos_principales(base_dir)
    crear_archivos_src(base_dir / "src")
    crear_notebooks(base_dir / "notebooks")
    crear_documentacion(base_dir / "docs")
    crear_ejemplos(base_dir / "examples")
    crear_tests(base_dir / "tests")
    crear_configuracion(base_dir / "config")
    crear_scripts(base_dir / "scripts")
    
    print("\n" + "=" * 60)
    print("✅ ¡Estructura del repositorio creada exitosamente!")
    print(f"📂 Directorio: {base_dir.absolute()}")
    print("\n🎯 Próximos pasos:")
    print(f"   cd {nombre_proyecto}")
    print("   pip install -r requirements.txt")
    print("   python scripts/setup_env.py")
    
def crear_archivos_principales(base_dir):
    """Crea archivos principales del repositorio"""
    
    # README.md
    readme_content = """# 🤖 PDF Comparator with Chatbot AI

> Sistema inteligente para comparar documentos PDF usando múltiples técnicas de IA y un chatbot conversacional.

## 🚀 Instalación Rápida

```bash
# Instalar dependencias
pip install -r requirements.txt

# Configurar entorno
python scripts/setup_env.py

# Ejecutar chatbot de consola
python src/main.py --mode console

# Ejecutar interfaz web
streamlit run src/streamlit_app.py
```

## 📚 Documentación

- [Guía de Usuario](docs/user_guide.md)
- [API Documentation](docs/api_docs.md)
- [Configuración](docs/configuration.md)

## 🎯 Características

- ✅ Múltiples técnicas de análisis de IA
- ✅ Chatbot conversacional inteligente  
- ✅ Interfaces web modernas
- ✅ API REST completa
- ✅ Soporte para múltiples LLMs

Ver documentación completa en [docs/](docs/)
"""
    
    # requirements.txt
    requirements = """# Core dependencies
PyPDF2>=3.0.1
sentence-transformers>=2.2.2
scikit-learn>=1.3.0
nltk>=3.8.1
pandas>=2.0.3
numpy>=1.24.3
matplotlib>=3.7.2
seaborn>=0.12.2

# LangChain
langchain>=0.0.350
langchain-community>=0.0.10
langchain-openai>=0.0.5

# Web interfaces
streamlit>=1.28.0
gradio>=4.0.0
fastapi>=0.104.0
uvicorn>=0.24.0

# vLLM (optional)
# vllm>=0.2.0

# Messaging integrations (optional)
# python-telegram-bot>=20.0
# twilio>=8.0.0

# Development tools
pytest>=7.4.0
black>=23.0.0
flake8>=6.0.0
mypy>=1.5.0

# Additional utilities
python-dotenv>=1.0.0
pydantic>=2.4.0
"""
    
    # .gitignore
    gitignore = """.env
.env.local
.env.production

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Project specific
data/pdfs/*.pdf
data/results/*.json
temp/
logs/
*.log
models/
checkpoints/
"""
    
    # LICENSE
    license_content = """MIT License

Copyright (c) 2024 PDF Comparator Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    
    # Crear archivos
    archivos = {
        "README.md": readme_content,
        "requirements.txt": requirements,
        ".gitignore": gitignore,
        "LICENSE": license_content
    }
    
    for nombre, contenido in archivos.items():
        archivo_path = base_dir / nombre
        archivo_path.write_text(contenido, encoding='utf-8')
        print(f"📄 Creado: {nombre}")

def crear_archivos_src(src_dir):
    """Crea archivos del directorio src/"""
    
    # main.py
    main_content = '''#!/usr/bin/env python3
"""
Punto de entrada principal del sistema de comparación de PDFs
"""

import argparse
import sys
from pathlib import Path

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent))

from chatbot_core import ChatbotManager
from console_chatbot import ejecutar_chatbot_consola
from pdf_comparator import verificar_estado_sistema

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(description="PDF Comparator with Chatbot AI")
    parser.add_argument("--mode", choices=["console", "web", "api"], 
                       default="console", help="Modo de ejecución")
    parser.add_argument("--llm", choices=["vllm", "openai", "ollama"], 
                       default="vllm", help="Proveedor LLM")
    parser.add_argument("--pdf1", help="Ruta al primer PDF")
    parser.add_argument("--pdf2", help="Ruta al segundo PDF")
    
    args = parser.parse_args()
    
    print("🤖 PDF Comparator with Chatbot AI")
    print("=" * 40)
    
    # Verificar sistema
    if not verificar_estado_sistema():
        print("❌ Sistema no está listo. Revisa la configuración.")
        return 1
    
    # Configurar manager
    manager = ChatbotManager()
    manager.configurar(llm_provider=args.llm)
    
    if args.mode == "console":
        print("🖥️ Iniciando chatbot de consola...")
        ejecutar_chatbot_consola()
    elif args.mode == "web":
        print("🌐 Para interfaz web, ejecuta:")
        print("   streamlit run src/streamlit_app.py")
    elif args.mode == "api":
        print("🚀 Para API REST, ejecuta:")
        print("   uvicorn src.fastapi_app:app --reload")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
'''
    
    # __init__.py
    init_content = '''"""
PDF Comparator with Chatbot AI
Sistema inteligente para comparar documentos PDF
"""

__version__ = "1.0.0"
__author__ = "PDF Comparator Team"
__email__ = "team@pdfcomparator.com"

from .pdf_comparator import *
from .chatbot_core import *
'''
    
    # config.py
    config_content = '''"""
Configuración global del sistema
"""

import os
from pathlib import Path
from typing import Dict, Any

# Directorios base
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = DATA_DIR / "results"
MODELS_DIR = BASE_DIR / "models"

# Configuración por defecto
DEFAULT_CONFIG = {
    "llm_provider": "vllm",
    "max_file_size": 50 * 1024 * 1024,  # 50MB
    "supported_formats": [".pdf"],
    "temp_dir": "/tmp/pdf_comparator",
    "log_level": "INFO"
}

# Configuración de modelos
MODEL_CONFIGS = {
    "vllm": {
        "host": "localhost",
        "port": 8000,
        "model": "meta-llama/Llama-2-7b-chat-hf",
        "temperature": 0.3,
        "max_tokens": 2048
    },
    "openai": {
        "model": "gpt-3.5-turbo",
        "temperature": 0.3,
        "max_tokens": 2048
    },
    "ollama": {
        "host": "localhost", 
        "port": 11434,
        "model": "llama2",
        "temperature": 0.3
    }
}

def get_config() -> Dict[str, Any]:
    """Obtiene configuración del sistema"""
    config = DEFAULT_CONFIG.copy()
    
    # Sobrescribir con variables de entorno
    if os.getenv("LLM_PROVIDER"):
        config["llm_provider"] = os.getenv("LLM_PROVIDER")
    
    return config
'''
    
    archivos_src = {
        "main.py": main_content,
        "__init__.py": init_content,
        "config.py": config_content,
        "pdf_comparator.py": "# Código del comparador PDF (importar desde notebooks)",
        "chatbot_core.py": "# Código del chatbot core (importar desde notebooks)",
        "console_chatbot.py": "# Código del chatbot de consola",
        "streamlit_app.py": "# Aplicación Streamlit",
        "gradio_app.py": "# Aplicación Gradio", 
        "fastapi_app.py": "# API REST con FastAPI",
        "telegram_bot.py": "# Bot de Telegram",
        "whatsapp_bot.py": "# Bot de WhatsApp",
        "utils.py": "# Utilidades generales"
    }
    
    for nombre, contenido in archivos_src.items():
        archivo_path = src_dir / nombre
        archivo_path.write_text(contenido, encoding='utf-8')
        print(f"🐍 Creado: src/{nombre}")

def crear_notebooks(notebooks_dir):
    """Crea notebooks de ejemplo"""
    
    notebooks = {
        "01_pdf_comparator_basic.ipynb": "# Notebook básico del comparador PDF",
        "02_chatbot_integration.ipynb": "# Notebook de integración del chatbot", 
        "03_langchain_setup.ipynb": "# Notebook de configuración LangChain",
        "04_web_interfaces.ipynb": "# Notebook de interfaces web",
        "05_api_examples.ipynb": "# Notebook de ejemplos API",
        "99_complete_demo.ipynb": "# Demo completa del sistema"
    }
    
    for nombre, contenido in notebooks.items():
        archivo_path = notebooks_dir / nombre
        archivo_path.write_text(contenido, encoding='utf-8')
        print(f"📓 Creado: notebooks/{nombre}")

def crear_documentacion(docs_dir):
    """Crea documentación del proyecto"""
    
    # user_guide.md
    user_guide = """# 📖 Guía de Usuario

## Introducción
Esta guía te ayudará a usar el sistema de comparación de PDFs con chatbot IA.

## Instalación
Ver [README.md](../README.md) para instrucciones de instalación.

## Uso Básico

### Chatbot de Consola
```bash
python src/main.py --mode console
```

### Interfaz Web
```bash
streamlit run src/streamlit_app.py
```

## Comandos del Chatbot
- `/start` - Iniciar nueva comparación
- `/help` - Mostrar ayuda
- `/status` - Ver estado actual
- `/reset` - Reiniciar sesión

## Tipos de Análisis
- **Rápido** - Análisis básico
- **Completo** - Análisis detallado
- **Legal** - Documentos legales
- **Técnico** - Documentación técnica
- **Académico** - Papers científicos
"""
    
    # api_docs.md
    api_docs = """# 🚀 Documentación API

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
curl -X POST "http://localhost:8000/chat" \\
     -H "Content-Type: application/json" \\
     -d '{"session_id": "user123", "message": "hola"}'
```
"""
    
    # configuration.md
    configuration = """# ⚙️ Configuración

## Variables de Entorno

```bash
# LLM Provider
LLM_PROVIDER=vllm

# OpenAI
OPENAI_API_KEY=tu_api_key

# Telegram
TELEGRAM_BOT_TOKEN=tu_token

# Twilio/WhatsApp
TWILIO_ACCOUNT_SID=tu_sid
TWILIO_AUTH_TOKEN=tu_token
```

## Configuración de Modelos

### vLLM Local
```bash
python -m vllm.entrypoints.openai.api_server \\
  --model meta-llama/Llama-2-7b-chat-hf \\
  --host localhost \\
  --port 8000
```

### Ollama
```bash
ollama serve
ollama pull llama2
```

## Archivos de Configuración

Ver `config/` para ejemplos de configuración.
"""
    
    docs = {
        "user_guide.md": user_guide,
        "api_docs.md": api_docs, 
        "configuration.md": configuration,
        "troubleshooting.md": "# 🔧 Solución de Problemas\\n\\nProblemas comunes y soluciones.",
        "contributing.md": "# 🤝 Contribuciones\\n\\nGuía para contribuir al proyecto.",
        "changelog.md": "# 📝 Changelog\\n\\n## v1.0.0\\n- Versión inicial"
    }
    
    for nombre, contenido in docs.items():
        archivo_path = docs_dir / nombre
        archivo_path.write_text(contenido, encoding='utf-8')
        print(f"📄 Creado: docs/{nombre}")

def crear_ejemplos(examples_dir):
    """Crea archivos de ejemplo"""
    
    # example_usage.py
    example_usage = '''"""
Ejemplos de uso del sistema
"""

from src.chatbot_core import ChatbotManager
from src.pdf_comparator import comparar_pdfs_completo

def ejemplo_basico():
    """Ejemplo básico de comparación"""
    # Configurar manager
    manager = ChatbotManager()
    
    # Crear chatbot
    chatbot = manager.crear_chatbot_consola()
    
    # Iniciar chat
    chatbot.iniciar_chat()

def ejemplo_api():
    """Ejemplo de uso de API"""
    import requests
    
    # Enviar mensaje
    response = requests.post("http://localhost:8000/chat", json={
        "session_id": "ejemplo",
        "message": "hola"
    })
    
    print(response.json())

if __name__ == "__main__":
    ejemplo_basico()
'''
    
    # sample_config.env
    sample_env = """# Configuración de ejemplo
# Copia este archivo a .env y configura tus valores

# LLM Provider (vllm, openai, ollama)
LLM_PROVIDER=vllm

# OpenAI (opcional)
OPENAI_API_KEY=sk-your-openai-api-key-here

# Telegram Bot (opcional)
TELEGRAM_BOT_TOKEN=your-telegram-bot-token

# Twilio/WhatsApp (opcional)
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-token
TWILIO_WHATSAPP_NUMBER=+1234567890

# Configuración del sistema
MAX_FILE_SIZE=52428800
LOG_LEVEL=INFO
"""
    
    ejemplos = {
        "example_usage.py": example_usage,
        "sample_config.env": sample_env,
        "README.md": "# 📋 Ejemplos\\n\\nEjemplos de uso del sistema.",
        "sample_document1.txt": "Documento de ejemplo 1 (reemplazar con PDF real)",
        "sample_document2.txt": "Documento de ejemplo 2 (reemplazar con PDF real)"
    }
    
    for nombre, contenido in ejemplos.items():
        archivo_path = examples_dir / nombre
        archivo_path.write_text(contenido, encoding='utf-8')
        print(f"📋 Creado: examples/{nombre}")

def crear_tests(tests_dir):
    """Crea archivos de test"""
    
    tests = {
        "__init__.py": "",
        "test_pdf_comparator.py": "# Tests del comparador PDF",
        "test_chatbot.py": "# Tests del chatbot",
        "test_api.py": "# Tests de la API",
        "conftest.py": "# Configuración de pytest",
        "README.md": "# 🧪 Tests\\n\\nSuite de tests del proyecto."
    }
    
    for nombre, contenido in tests.items():
        archivo_path = tests_dir / nombre
        archivo_path.write_text(contenido, encoding='utf-8')
        print(f"🧪 Creado: tests/{nombre}")

def crear_configuracion(config_dir):
    """Crea archivos de configuración"""
    
    # config.json
    config_json = {
        "app": {
            "name": "PDF Comparator Chatbot",
            "version": "1.0.0",
            "debug": False
        },
        "llm": {
            "default_provider": "vllm",
            "timeout": 120,
            "max_retries": 3
        },
        "chatbot": {
            "max_session_time": 3600,
            "max_file_size": 52428800
        },
        "logging": {
            "level": "INFO",
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    }
    
    configs = {
        "config.json": json.dumps(config_json, indent=2),
        "logging.conf": "# Configuración de logging",
        "model_configs.yaml": "# Configuraciones de modelos",
        "README.md": "# ⚙️ Configuración\\n\\nArchivos de configuración del sistema."
    }
    
    for nombre, contenido in configs.items():
        archivo_path = config_dir / nombre
        if nombre.endswith('.json'):
            archivo_path.write_text(contenido, encoding='utf-8')
        else:
            archivo_path.write_text(contenido, encoding='utf-8')
        print(f"⚙️ Creado: config/{nombre}")

def crear_scripts(scripts_dir):
    """Crea scripts de utilidad"""
    
    # setup_env.py
    setup_env = '''#!/usr/bin/env python3
"""
Script para configurar el entorno de desarrollo
"""

import os
import sys
from pathlib import Path

def setup_environment():
    """Configura el entorno"""
    print("🔧 Configurando entorno...")
    
    # Crear directorios necesarios
    dirs = ["logs", "temp", "data/pdfs", "data/results"]
    for dir_name in dirs:
        Path(dir_name).mkdir(parents=True, exist_ok=True)
        print(f"📁 Directorio creado: {dir_name}")
    
    # Verificar Python
    if sys.version_info < (3, 8):
        print("❌ Se requiere Python 3.8 o superior")
        return False
    
    print("✅ Entorno configurado correctamente")
    return True

if __name__ == "__main__":
    setup_environment()
'''
    
    # install_deps.py
    install_deps = '''#!/usr/bin/env python3
"""
Script para instalar dependencias
"""

import subprocess
import sys

def install_dependencies():
    """Instala dependencias"""
    print("📦 Instalando dependencias...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencias instaladas")
    except subprocess.CalledProcessError:
        print("❌ Error instalando dependencias")
        return False
    
    return True

if __name__ == "__main__":
    install_dependencies()
'''
    
    scripts = {
        "setup_env.py": setup_env,
        "install_deps.py": install_deps,
        "run_tests.py": "# Script para ejecutar tests",
        "deploy.py": "# Script de deployment",
        "backup.py": "# Script de backup",
        "README.md": "# 🔧 Scripts\\n\\nScripts de utilidad del proyecto."
    }
    
    for nombre, contenido in scripts.items():
        archivo_path = scripts_dir / nombre
        archivo_path.write_text(contenido, encoding='utf-8')
        if nombre.endswith('.py'):
            # Hacer ejecutable en Unix
            try:
                os.chmod(archivo_path, 0o755)
            except:
                pass
        print(f"🔧 Creado: scripts/{nombre}")

def main():
    """Función principal del script"""
    nombre_proyecto = sys.argv[1] if len(sys.argv) > 1 else "pdf-comparator-chatbot"
    
    print("🤖 PDF Comparator - Setup Repository")
    print("=" * 60)
    
    try:
        crear_estructura_repositorio(nombre_proyecto)
        
        print("\n🎯 Estructura creada exitosamente!")
        print(f"📂 Navega a: cd {nombre_proyecto}")
        print("🚀 Sigue las instrucciones del README.md")
        
    except Exception as e:
        print(f"❌ Error creando estructura: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())