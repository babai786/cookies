from django.shortcuts import render

def name_view(request):
    return render(request,'pratikapp/name.html')

def age_view(request):
    name=request.GET['name']
    response=render(request,'pratikapp/age.html')
    response.set_cookie('name',name)
    return response

def gfname_view(request):
    age=request.GET['age']
    response=render(request,'pratikapp/gfname.html')
    response.set_cookie('age',age)
    return response

def result(request):
    gfname=request.GET['gfname']
    name=request.COOKIES.get('name',0)
    age=request.COOKIES.get('age',0)
    response=render(request,'pratikapp/result.html',{'name':name,'age':age,'gfname':gfname})

    return response
