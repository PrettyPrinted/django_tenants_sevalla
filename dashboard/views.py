from django.http import HttpResponse

def index(request):
    return HttpResponse(f"Hello, {request.tenant.name} this is the tenant-specific view!")