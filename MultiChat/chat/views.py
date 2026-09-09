from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.
def chat_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get('message')
        return JsonResponse({'response': "Your Message: " + message})
    return render(request, 'navigator-chat.html')