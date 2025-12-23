import base64
from pathlib import Path

def image_to_base64(image_path: str, output_file: str):
    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(f"No existe el archivo: {image_path}")

    with open(image_path, "rb") as img_file:
        encoded_bytes = base64.b64encode(img_file.read())
        encoded_str = encoded_bytes.decode("utf-8")

    mime_type = "image/png" if image_path.suffix.lower() == ".png" else "image/jpeg"

    html_img = f'<img src="data:{mime_type};base64,{encoded_str}" alt="Foto Profesional">'

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_img)

    print("✅ Base64 generado correctamente")
    print(f"📄 Archivo HTML listo: {output_file}")
    print(f"📦 Tamaño Base64: {len(encoded_str) / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    # Ajusta estas rutas
    IMAGE_PATH = "...//profile.png"
    OUTPUT_FILE = "...//cvTemplate//profile_base64.html"

    image_to_base64(IMAGE_PATH, OUTPUT_FILE)
