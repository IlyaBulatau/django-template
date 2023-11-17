from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render


def healthcheck(request):

    context = {'status': 'OK'}
    return HttpResponse(
        render(request=request, template_name="index/index.html", context=context)
        )
