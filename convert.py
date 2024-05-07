def convert_exif_to_dict(exif_data):
    converted_exif = {}
    for key, value in exif_data.items():
        if isinstance(value, bytes):
            converted_exif[key] = str(value, 'utf-8', 'ignore')
        elif isinstance(value, (int, float, str)):
            converted_exif[key] = value
    return converted_exif