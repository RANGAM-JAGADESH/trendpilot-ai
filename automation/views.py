from django.http import HttpResponse

def home(request):
    return HttpResponse("TrendPilot AI is running 🚀")