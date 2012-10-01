#from django.http import HttpResponse
from myblog.models import Articles,Comments
from django.shortcuts import render_to_response
from datetime import *
#from django.template import Template,Context
#from django.template.loader import get_template

def index(request):
    a_list = Articles.objects.filter(deleted = False)
    count = len(a_list)
    if count > 5:
        b_list = a_list[:5]
    else:
        b_list = a_list
    c_list = []
    for k in a_list:
        c_list.append(k.tag)
    c_list = list(set(c_list))
    d_list = []
    for k in a_list:
        d_list.append(k.cdt)
    d_list = list(set(d_list))
    #fp = open('index.html')
    #t = get_template('index.html')
    #fp.close()
    #html = t.render(Context({'a_list':a_list}))
    #return HttpResponse(html)
    return render_to_response('index.html',{'a_list':a_list,'b_list':b_list,'c_list':c_list,'d_list':d_list,'title':True})

def articles(request,p_id):
    a_list = Articles.objects.filter(deleted = False)
    count = len(a_list)
    if count > 5:
        b_list = a_list[:5]
    else:
        b_list = a_list
    c_list = []
    for k in a_list:
        c_list.append(k.tag)
    c_list = list(set(c_list))
    d_list = []
    for k in a_list:
        d_list.append(k.cdt)
    d_list = list(set(d_list))
    p = Articles.objects.get(id = p_id)
    e_list = Comments.objects.filter(articles = p)
    errors = []
    if request.method == 'POST':
        if not request.POST.get('author',''):
            errors.append('Enter name!')
        if not request.POST.get('email','') or '@' not in request.POST['email']:
            errors.append('Enter email address!')
        if not request.POST.get('comment',''):
            errors.append('Enter your comments!')
        if not errors:
            new = Comments(articles = p,name = request.POST['author'],dt=datetime.now(),email = request.POST['email'],text=request.POST['comment'],deleted = False)
            new.save()
            p.cn = p.cn+1
            p.save()
            errors.append('Success!')
            return render_to_response('articles.html',{'list':p,'b_list':b_list,'c_list':c_list,'d_list':d_list,'e_list':e_list,'errors':errors})
        return render_to_response('articles.html',{'list':p,'b_list':b_list,'c_list':c_list,'d_list':d_list,'e_list':e_list,'errors':errors,'name':request.POST['author'],'email':request.POST['email'],'comment':request.POST['comment']})
    else:
        return render_to_response('articles.html',{'list':p,'b_list':b_list,'c_list':c_list,'d_list':d_list,'e_list':e_list})

def tag(request,p_tag):
    a_list = Articles.objects.filter(deleted = False)
    count = len(a_list)
    if count > 5:
        b_list = a_list[:5]
    else:
        b_list = a_list
    c_list = []
    for k in a_list:
        c_list.append(k.tag)
    c_list = list(set(c_list))
    d_list = []
    for k in a_list:
        d_list.append(k.cdt)
    d_list = list(set(d_list))
    e_list = Articles.objects.filter(deleted = False,tag = p_tag)
    #fp = open('index.html')
    #t = get_template('index.html')
    #fp.close()
    #html = t.render(Context({'a_list':a_list}))
    #return HttpResponse(html)
    return render_to_response('index.html',{'a_list':e_list,'b_list':b_list,'c_list':c_list,'d_list':d_list,'title':False})

def cdt(request,p_cdt):
    a_list = Articles.objects.filter(deleted = False)
    count = len(a_list)
    if count > 5:
        b_list = a_list[:5]
    else:
        b_list = a_list
    c_list = []
    for k in a_list:
        c_list.append(k.tag)
    c_list = list(set(c_list))
    d_list = []
    for k in a_list:
        d_list.append(k.cdt)
    d_list = list(set(d_list))
    e_list = Articles.objects.filter(deleted = False,cdt = p_cdt)
    #fp = open('index.html')
    #t = get_template('index.html')
    #fp.close()
    #html = t.render(Context({'a_list':a_list}))
    #return HttpResponse(html)
    return render_to_response('index.html',{'a_list':e_list,'b_list':b_list,'c_list':c_list,'d_list':d_list,'title':False})

def about(request):
    a_list = Articles.objects.filter(deleted = False)
    count = len(a_list)
    if count > 5:
        b_list = a_list[:5]
    else:
        b_list = a_list
    c_list = []
    for k in a_list:
        c_list.append(k.tag)
    c_list = list(set(c_list))
    d_list = []
    for k in a_list:
        d_list.append(k.cdt)
    d_list = list(set(d_list))
    #fp = open('index.html')
    #t = get_template('index.html')
    #fp.close()
    #html = t.render(Context({'a_list':a_list}))
    #return HttpResponse(html)
    return render_to_response('about.html',{'a_list':a_list,'b_list':b_list,'c_list':c_list,'d_list':d_list})



