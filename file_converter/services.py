import os
import pandas as pd
import json
from django.conf import settings


def convert_file(uploaded_file_path, original_extension, converted_folder):
    # converted_folder = os.path.join(settings.MEDIA_ROOT, "converted")
    os.makedirs(converted_folder, exist_ok=True)
    converted_files = {}

    if original_extension in ['csv', 'txt']:
        df = pd.read_csv(uploaded_file_path)
    elif original_extension in ['xls', 'xlsx']:
        df = pd.read_excel(uploaded_file_path)
    elif original_extension == 'json':
        with open(uploaded_file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            df = pd.json_normalize(json_data)  

    base_filename = os.path.splitext(os.path.basename(uploaded_file_path))[0]
    
    csv_path = os.path.join(converted_folder, f"{base_filename}.csv")
    df.to_csv(csv_path, index=False)
    converted_files['csv'] = csv_path

    excel_path = os.path.join(converted_folder, f"{base_filename}.xlsx")
    df.to_excel(excel_path, index=False)
    converted_files['excel'] = excel_path

    json_path = os.path.join(converted_folder, f"{base_filename}.json")
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(df.to_dict(orient='records'), json_file, indent=4)
    converted_files['json'] = json_path

    return converted_files