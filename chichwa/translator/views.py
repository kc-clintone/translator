import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .translator import translate


def home(request):
    return render(request, "index.html")


@csrf_exempt
def translate_text(request):
    if request.method == "POST":
        data = json.loads(request.body)

        text = data.get("text", "")
        target = data.get("targetLanguage", "sw")

        translated = translate(text, target)

        return JsonResponse({
            "translatedText": translated
        })

    return JsonResponse({"error": "POST request required"}, status=400)