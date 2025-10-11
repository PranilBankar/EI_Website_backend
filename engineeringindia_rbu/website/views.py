# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from website.supabase_client import supabase
# from django.shortcuts import redirect
# from django.http import JsonResponse
# @api_view(['GET'])
# def get_members(request):
#     data = supabase.table("members").select("*").execute()
#     return Response(data.data)

# @api_view(['GET'])
# def get_projects(request):
#     data = supabase.table("projects").select("*").execute()
#     return Response(data.data)

# @api_view(['GET'])
# def get_events(request):
#     data = supabase.table("events").select("*").execute()
#     return Response(data.data)
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1>Welcome to Engineering India RBU!</h1>")
#     return redirect('get_members')
# website/views.py
from django.shortcuts import redirect
from django.http import JsonResponse
from .supabase_client import supabase

# --- Redirect root URL to /api/members/ ---
def home(request):
    return redirect("https://engineeringindiarbu.netlify.app/")


# Example existing API endpoints
def get_members(request):
    # fetch members from Supabase
    data = supabase.table("members").select("*").execute()
    return JsonResponse(data.data, safe=False)

def get_projects(request):
    data = supabase.table("projects").select("*").execute()
    return JsonResponse(data.data, safe=False)

def get_events(request):
    data = supabase.table("events").select("*").execute()
    return JsonResponse(data.data, safe=False)
