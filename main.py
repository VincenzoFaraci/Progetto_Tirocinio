from fastapi import FastAPI, File, UploadFile,HTTPException
from PIL import Image
import json
from convert import convert_exif_to_dict
from get_metadata import get_metadata

app = FastAPI(title="Get file metadata")

@app.post("/files/")
async def metadata(file: UploadFile = File(...)):
    try:
        metadata_result = await get_metadata(file)
        return metadata_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))