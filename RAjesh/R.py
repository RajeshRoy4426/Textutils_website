
from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render (request,'home.html')
def Analysetext(request):
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    uppercase=request.POST.get('uppercase', 'off')
    lowcase=request.POST.get('lowcase', 'off')
    charcount=request.POST.get('charcount', 'off')
    newline=request.POST.get('newline', 'off')
    extraspace=request.POST.get('extraspace', 'off')
    count=0
    org=djtext
    if removepunc== "on":
        panc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        opt=""
        for char in djtext:
            if char not in panc:
                opt=opt+char    
                     
    dict={'given': org , 'analyized':opt}
    djtext=opt                          
    if (uppercase=="on"):
        opt=""
        for char in djtext:
            opt=opt+char.upper()
    dict={'given': org , 'analyized':opt}
    djtext=opt      
    if (lowcase=="on"):
        opt=""
        for char in djtext:
            opt=opt+char.lower()
    dict={'given': org , 'analyized':opt}
    djtext=opt     
    if (charcount=="on"):
        for char in djtext:
            count+=1
        dict={'given': org , 'analyized':count}    
        return render(request,'analyzed.html',dict)   
    if (extraspace=="on"):
        opt=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                opt=opt+char
    dict={'given': org , 'analyized':opt}
    djtext=opt 
    if (newline=="on"):
        opt=""
        for char in djtext:
            if (char !="\n" and char !="\r"):
                opt=opt+char
    print("pre", opt)            
    dict={'given': org , 'analyized':opt}         
    if(removepunc== "off" and uppercase=="off" and extraspace=="off" and newline=="off" and charcount=="off" and lowcase=="off"):
        return HttpResponse( "<h1> Error.... Select a valid option</h1>")
    return render(request,'analyzed.html',dict)    
#def CapFirst(request):
#    return HttpResponse('''<h1> Capfirst </h1>''')
#def SpaceRemove(request):
#    return HttpResponse('''<h1> Space remover </h1> <a href = " https://www.instagram.com/"> Click Here </a>''')
#def CharCount(request):
#   return HttpResponse('''<h1> char count </h1> <a href = " http://127.0.0.1:8000/"> Click Here </a>''')
#def NewlineRemove(request):
#     return HttpResponse('''<h1> newline remove</h1> <a href = " http://127.0.0.1:8000/"> Click Here </a>''')
