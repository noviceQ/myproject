# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
def search_form(request):
    return render_to_response('../templates/search_form.html')
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的：' + request.GET['q'].encode('utf-8')
    else:
        message = '你提交的表单为空'
    return HttpResponse(message)
