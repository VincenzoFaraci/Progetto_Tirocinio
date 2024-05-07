from fastapi import FastAPI, File, UploadFile
from PIL import Image
import json
from convert import convert_exif_to_dict


async def get_metadata(file: UploadFile = File(...)):
    data = {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_MB": file.size / (1024*1024)
    }
    try:
        if file.content_type.startswith('image'):
            with Image.open(file.file) as img:
                exif_data = img._getexif()
                if exif_data:
                    cleaned_exif = convert_exif_to_dict(exif_data)
                    data["exif_data"] = cleaned_exif
        elif file.content_type.startswith('text'):
            with file.file as f:
                text_content = f.read().decode('utf-8')
            data["text_content"] = text_content
        elif file.content_type.startswith('video'):
            pass
        else:
            data["error"] = "Tipo di file non supportato"
    except Exception as e:
        data["error"] = f"Errore durante l'elaborazione del file: {e}"

    return data