from django.shortcuts import render

def count_view(request):
    count=int(request.COOKIES.get('count',0))
    newcount=count+1
    response=render(request,'pratikapp/cookie.html',{'count':newcount})
    response.set_cookie('count',newcount)
    return response
