from django.http import HttpResponse
from django.shortcuts import render

# important concept
# Laying the pipeline
#     creating function in view and creating routing for the same in url.py file

# templating
# sending html page in respose


def index(request):
    return render(request, 'index.html', {'name': 'prathmesh', 'place': 'new zeland'})
    # return HttpResponse('<a href="https://www.google.com"> <h1>hello jack</h1> </a>')


def about(request):
    return HttpResponse('about jack bhai')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    remove_space = request.POST.get('remove_space', 'default')
    upper = request.POST.get('upper', 'default')
    remove_punc = request.POST.get('remove_punc', 'default')
    print(djtext)
    print(remove_space)
    print(upper)
    print(remove_punc)

    if remove_space == 'on':
        normalText = ""
        for index, i in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                normalText = normalText + i
        return render(request, 'analyze.html', {'originaltext': djtext, 'modifiedtext': normalText})

    elif remove_punc == 'on':
        normalText = ""
        puncArr = {'!', '@', '#', '"', '', '$', '%', '^', '&',
                   '*', '(', ')', '-', '_', '+', '=', '`', '`', }
        for i in djtext:
            if i not in puncArr:
                normalText = normalText + i
        params = {'originaltext': djtext, 'modifiedtext': normalText}
        return render(request, 'analyze.html', params)

    elif upper == 'on':
        return render(request, 'analyze.html', {'originaltext': djtext, 'modifiedtext': djtext.upper()})

    else:
        return HttpResponse("bhai koi radio button to select kr")
