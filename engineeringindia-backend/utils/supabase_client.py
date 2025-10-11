# utils/supabase_client.py
import requests
from django.conf import settings

BUCKET = "public"  # create this bucket in Supabase storage or edit accordingly

def upload_file_to_supabase(file_obj, dest_path: str, content_type: str = None):
    """
    file_obj: Django UploadedFile or bytes
    dest_path: 'events/banner.jpg'
    returns: public_url (string)
    """
    url = f"{settings.SUPABASE_URL}/storage/v1/object/{BUCKET}/{dest_path}"
    headers = {
        "Authorization": f"Bearer {settings.SUPABASE_SERVICE_ROLE_KEY}",
        "x-upsert": "true",
    }
    if content_type:
        headers["Content-Type"] = content_type
    if hasattr(file_obj, "read"):
        data = file_obj.read()
    else:
        data = file_obj
    resp = requests.put(url, headers=headers, data=data)
    resp.raise_for_status()
    public_url = f"{settings.SUPABASE_URL}/storage/v1/object/public/{BUCKET}/{dest_path}"
    return public_url
