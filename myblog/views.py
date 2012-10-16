#from django.http import HttpResponse
from models import Articles,Comments
from django.shortcuts import render_to_response
from datetime import *
from markdown import markdown
from cgi import escape
#from django.template import Template,Context
#from django.template.loader import get_template

def index(request,page=1):
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
    for z in a_list:
        z.text=markdown(z.text)
    r = 0
    r = r + (int(page)-1)*10
    p_list = []
    if len(a_list) > 10:
        if r+10 < len(a_list):
            for k in xrange(r,r+10):
                p_list.append(a_list[k])
        else:
            for k in xrange(r,len(a_list)):
                p_list.append(a_list[k])
    else:
        p_list = a_list
    #fp = open('index.html')
    #t = get_template('index.html')
    #fp.close()
    #html = t.render(Context({'a_list':a_list}))
    #return HttpResponse(html)
    pa = len(a_list)/10
    if len(a_list)%10 == 0:
        pa = pa-1
    return render_to_response('index.html',{'a_list':p_list,'b_list':b_list,'c_list':c_list,'d_list':d_list,'title':True,'f_list':range(1,pa+2),'type':'index'})

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
    p.text = markdown(p.text)
    e_list = Comments.objects.filter(articles = p)
    for k in e_list:
        k.text = k.text.replace('\n','</br>')
    errors = []
    if request.method == 'POST':
        if not request.POST.get('author',''):
            errors.append('Enter name!')
        if not request.POST.get('email','') or '@' not in request.POST['email']:
            errors.append('Enter email address!')
        if not request.POST.get('comment',''):
            errors.append('Enter your comments!')
        if not errors:
            new = Comments(articles = p,name = request.POST['author'],dt=datetime.now(),email = request.POST['email'],text=escape(request.POST['comment']),deleted = False)
            new.save()
            p.cn = p.cn+1
            p.save()
            errors.append('Success!')
            return render_to_response('articles.html',{'list':p,'b_list':b_list,'c_list':c_list,'d_list':d_list,'e_list':e_list,'errors':errors})
        return render_to_response('articles.html',{'list':p,'b_list':b_list,'c_list':c_list,'d_list':d_list,'e_list':e_list,'errors':errors,'name':request.POST['author'],'email':request.POST['email'],'comment':request.POST['comment']})
    else:
        return render_to_response('articles.html',{'list':p,'b_list':b_list,'c_list':c_list,'d_list':d_list,'e_list':e_list})

def tag(request,p_tag,page=1):
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
    for z in e_list:
        z.text = markdown(z.text)
    r = 0
    r = r + (int(page)-1)*10
    p_list = []
    if len(e_list) > 10:
        if r+10 < len(e_list):
            for k in xrange(r,r+10):
               p_list.append(e_list[k])
        else:
            for k in xrange(r,len(e_list)):
                p_list.append(e_list[k])
    else:
        p_list = e_list
    #fp = open('index.html')
    #t = get_template('index.html')
    #fp.close()
    #html = t.render(Context({'a_list':a_list}))
    #return HttpResponse(html)
    pa = len(e_list)/10
    if len(e_list)%10 == 0:
        pa = pa-1
    t = 'tag/'+p_tag
    return render_to_response('index.html',{'a_list':p_list,'b_list':b_list,'c_list':c_list,'d_list':d_list,'f_list':range(1,pa+2),'title':False,'type':t})

def cdt(request,p_cdt,page=1):
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
    for z in e_list:
        z.text = markdown(z.text)
    r = 0
    r = r + (int(page)-1)*10
    p_list = []
    if len(e_list) > 10:
        if r+10 < len(e_list):
            for k in xrange(r,r+10):
                p_list.append(e_list[k])
        else:
            for k in xrange(r,len(e_list)):
                p_list.append(e_list[k])
    else:
        p_list = e_list
    #fp = open('index.html')
    #t = get_template('index.html')
    #fp.close()
    #html = t.render(Context({'a_list':a_list}))
    #return HttpResponse(html)
    pa = len(e_list)/10
    if len(e_list)%10 == 0:
        pa = pa -1
    t = 'time/'+p_cdt
    return render_to_response('index.html',{'a_list':p_list,'b_list':b_list,'c_list':c_list,'d_list':d_list,'f_list':range(1,pa+2),'title':False,'type':t})

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



