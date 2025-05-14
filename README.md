# OrganizAI

**OrganizAI** es una aplicación diseñada para ayudar a estudiantes a organizar su tiempo de estudio de forma eficiente mediante inteligencia artificial. Permite registrar tareas académicas, establecer disponibilidad horaria y generar cronogramas optimizados según reglas predefinidas.

## ✨ Características

- **Gestión de tareas**: Añade tareas con fecha de inicio, fin, duración estimada y prioridad.
- **Disponibilidad horaria**: Configura tus horarios disponibles para estudiar.
- **Generación automática de cronogramas**: Usa Google Gemini para crear un plan de estudio personalizado.
- **API REST**: Interfaz para integrar OrganizAI con otras aplicaciones.
- **Interfaz CLI**: Control total desde la terminal para usuarios avanzados.

## 🗂️ Estructura del Proyecto

```plaintext
organizai/
├── api/                # Endpoints de la API
├── models/             # Modelos de datos (tareas, disponibilidad)
├── prompts/            # Plantillas de prompts para la IA
├── services/           # Lógica de negocio (cliente Gemini, planificación)
├── utils/              # Utilidades (parsers, cargadores de prompts)
└── main.py             # Interfaz de línea de comandos
```

## ✅ Requisitos

- Python 3.11 o superior
- [Poetry](https://python-poetry.org/) para gestionar dependencias
- Clave API de Google Gemini definida en un archivo `.env`

## ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd organizai
   ```

2. Instala las dependencias con Poetry:
   ```bash
   poetry install
   ```

3. Configura tu clave API de Google Gemini:
   ```bash
   echo "GOOGLE_GEMINI_API_KEY=tu_clave_de_api" > .env
   ```

## 🚀 Uso

### CLI – Interfaz de Línea de Comandos

Ejecuta la aplicación desde la terminal:

```bash
poetry run organizai
```

### API REST

Inicia el servidor con FastAPI:

```bash
poetry run uvicorn organizai.api_app:app --reload
```

**Endpoint principal:**

```
POST /api/schedule/
```

**Ejemplo de solicitud:**

```json
{
  "tasks": [
    {
      "name": "Tarea 1",
      "start_date": "2025-05-13",
      "end_date": "2025-05-15",
      "estimated_hours": 4,
      "priority": 10
    },
    {
      "name": "Tarea 2",
      "start_date": "2025-05-14",
      "end_date": "2025-05-18",
      "estimated_hours": 5,
      "priority": 7
    }
  ],
  "availability": {
    "days": [
      {
        "day": "Monday",
        "time_ranges": [
          {"start_time": "10:00", "end_time": "12:00"},
          {"start_time": "15:00", "end_time": "18:00"}
        ]
      },
      {
        "day": "Tuesday",
        "time_ranges": [
          {"start_time": "09:00", "end_time": "12:00"}
        ]
      }
    ]
  }
}
```
