from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .src.index import get_available_moves
import json

@csrf_exempt # To excempt from the csrf request
def index(request,slug):
    try:
        if request.method == "POST":
            # Convert Body into json
            body = json.loads(request.body.decode("utf-8"))
            positions = body['positions']
            slug = slug.capitalize()
            response = get_available_moves(slug,positions)
            return JsonResponse({"valid_moves": response},status=200)
    except Exception as error:
        return JsonResponse({"Internal Server Error": error}, status=500)