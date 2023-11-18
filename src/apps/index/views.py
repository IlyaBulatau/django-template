from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render


def healthcheck(request):
    current_user = request.user
    context = {
        'status': 'OK',
        'current_user': current_user}
    
    return HttpResponse(
        render(request=request, template_name="index/index.html", context=context)
        )
