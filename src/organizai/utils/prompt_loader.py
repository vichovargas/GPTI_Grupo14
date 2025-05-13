from pathlib import Path

def load_prompt_template(name: str) -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / f"{name}.txt"
    return path.read_text(encoding="utf-8")
