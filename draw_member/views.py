from django.shortcuts import render
from datetime import datetime
from .models import Post
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
def myimg(request):
    image_data = open("childslide.png", "rb").read()
    return HttpResponse(image_data, mimetype = "image/png")

def search_form(request):
    return render(request, "search_form.html", { 'session_item' : request.session['member_id'] } )
    
def search(request):
    
    if request.method == 'GET':
        if 'q' in request.GET and request.GET['q']:
            str = request.GET['q']
            if len(str) > 5:
                xxx = "string to long"
            elif int(str) > 20:
                xxx = " %s more than 20" % str
            else:
                xxx = " %s less than 20" % str
        else:
            xxx = "999"
        
        return HttpResponseRedirect('/home/')
    
        #return render(request, "login_account.html", { 'current_time' : xxx } )

def second(request):
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknow'
    

    return render(request, "live.html", { 
        'hello' : "hello Welcome",
        'path': request.get_host(),
        'isSecure' : request.is_secure(),
        'method' : request.encoding,
        'agent' : ua
        } )
        
    
def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {'post_list': post_list } )
    
def addOne(request):
    add = Post.objects.create(title=request.GET['username'], content=request.GET['password'], location='tttt')
    add.save()
    return HttpResponse("insert one Ok")
    
def updateOne(request):
    Post.objects.filter(title=request.GET['username']).update(content=request.GET['password'])
    return HttpResponse("update one Ok")
    
def 刪除(request):
    m = Post.objects.get(title=request.GET['username'])
    m.delete()
    return HttpResponse("delete one Ok")
    
def login(request):
    try:
        m = Post.objects.get(title=request.GET['username'])
        if m.content == request.GET['password']:
            request.session['member_id'] = m.location
            return HttpResponse("Your username and password is right and Location %s" % m.location)
    except Post.DoesNotExist:
        return HttpResponse("Your username and password is error")

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        return HttpResponse("You are log out")
