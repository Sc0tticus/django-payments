# square/views.py

from django.http import JsonResponse
from square import Square
from square.environment import SquareEnvironment
from django.conf import settings  # so we can access settings.SQUARE_SANDBOX_ACCESS_TOKEN

client = Square(
    token=settings.SQUARE_SANDBOX_ACCESS_TOKEN,
    environment=SquareEnvironment.SANDBOX
)

def list_merchants(request):
    result = client.merchants.list_merchants()

    if result.is_success():
        return JsonResponse(result.body, safe=False)
    elif result.is_error():
        return JsonResponse({"errors": result.errors}, status=400)
