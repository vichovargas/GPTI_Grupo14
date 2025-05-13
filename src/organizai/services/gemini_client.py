import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise EnvironmentError("GOOGLE_API_KEY no está definido en el entorno.")

# Configurar el cliente Gemini
client = genai.Client(api_key=api_key)

# Modelo recomendado: rápido y económico
MODEL_NAME = "gemini-2.0-flash"

def call_gemini(prompt: str) -> str:
    """Envía un prompt a Gemini y devuelve el texto de respuesta."""
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[prompt],
            config=types.GenerateContentConfig(
                system_instruction="Actúas como un planificador académico experto que ayuda a estudiantes de ingeniería a organizar su tiempo de estudio.",
                temperature=0.7,
                max_output_tokens=1800,
            )
        )
        return response.text.strip()
    except Exception as e:
        return f"[ERROR] Fallo al comunicarse con Gemini: {e}"
