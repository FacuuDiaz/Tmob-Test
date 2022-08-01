# Django
from django.http import HttpResponse
# models
from apps.redirect.models import Redirect
# Utilites
import json


def get_url(request, key:str) -> dict:
    """ function: get_url

    Args:
        request (Request): Request object attatch to response http protocol
        key (str): identifier of a model instance

    Returns:
        HttpResponse: In two differents cases:
        - Case 1 (all good)
            dict: The data (key,url) of the instance matching with the key param 
            Example: 
            ```
            {
            "key": "1",
            "url": "localhost:8000"
            }
            ```   
        - Case 2 (don't exist)
            str: response of the non-existence of the match with the key entered in the request
    """
    data = Redirect.get_redirect(key)
    if data is None:
        return HttpResponse(f"Don't exist a Redirect instance with this key: '{key}'. \n Try again with another key", status=409)
    return HttpResponse(json.dumps(data, indent=4, ensure_ascii=False),content_type='application/json',status=200)