#!/usr/bin/env python3
"""
Genera archivos MP3 de podcast a partir de los scripts de texto.
Uso: python3 generar-audios.py
Requiere: pip install gtts
"""
import os
import glob
from gtts import gTTS

PODCAST_DIR = os.path.dirname(os.path.abspath(__file__))

def generar_audio(script_path):
    """Convierte un script .txt en un archivo .mp3"""
    base = os.path.splitext(os.path.basename(script_path))[0]
    mp3_name = base.replace("script-", "podcast-") + ".mp3"
    mp3_path = os.path.join(PODCAST_DIR, mp3_name)

    print(f"Leyendo: {script_path}")
    with open(script_path, "r", encoding="utf-8") as f:
        text = f.read()

    # gTTS tiene limite de caracteres, dividimos en bloques
    print(f"  Texto: {len(text)} caracteres")
    print(f"  Generando audio: {mp3_name}...")

    tts = gTTS(text=text, lang="es", tld="es", slow=False)
    tts.save(mp3_path)

    size_mb = os.path.getsize(mp3_path) / (1024 * 1024)
    print(f"  Guardado: {mp3_name} ({size_mb:.1f} MB)")
    return mp3_path

def main():
    scripts = sorted(glob.glob(os.path.join(PODCAST_DIR, "script-tema-*.txt")))

    if not scripts:
        print("No se encontraron scripts. Asegurate de tener archivos script-tema-XX.txt")
        return

    print(f"Encontrados {len(scripts)} scripts de podcast")
    print("=" * 50)

    generated = []
    for script in scripts:
        try:
            mp3 = generar_audio(script)
            generated.append(mp3)
        except Exception as e:
            print(f"  ERROR: {e}")

    print("=" * 50)
    print(f"Generados {len(generated)} podcasts:")
    for mp3 in generated:
        size_mb = os.path.getsize(mp3) / (1024 * 1024)
        print(f"  {os.path.basename(mp3)} ({size_mb:.1f} MB)")

if __name__ == "__main__":
    main()
