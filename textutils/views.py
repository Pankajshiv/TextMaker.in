# i have created this file.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html' )


def ForSimple(request):
    return HttpResponse(
     "<body style='background-color:yellow'>"
     "<img src=''>"
     "<h1>Hello with Pycharm</h1>"
     "<h3>Hi again</h3>"
     "<p style='color:red'>this is a paragraph</p>"
     "</body>"
    )

def about(request):
    return HttpResponse('''<h4>Hello about Pycharm</h4> <a href="https://www.hackerrank.com/dashboard">Go to HackerRank</a>''')

def ex1(request):
    return HttpResponse(
        '''
        <style>
        body{background-color:Cyan} </style>
        <center><h1>Websites Directories</h1>
        <table border='2' style='background-color:rgb(52,152,219)'>
        <tr><td>Websites</td><td><center>Information</center></td></tr>
        <tr><td><a href='https://www.hackerrank.com/dashboard' target='_blank'>HackerRank</a></td><td>Best learning website</td></tr>
        <tr><td><a href='https://www.youtube.com' target='_blank'>YouTube</a></td><td>You tube is a free video sharing websites that makes it easy to watch online videos</td></tr>
        <tr><td><a href='https://www.facebook.com' target='_blank'>Facebook</a></td><td>Social networking websites</td></tr>
        <tr><td><a href='https://www.google.com' target='_blank'>Google</a></td><td>Google is web-based tool that enables users to locate information on world wide web</td></tr>
        <tr><td><a href='https://www.linkedin.com' target='_blank'>LinkedIn</a><td>Best website for getting job opportunities</td></tr>
        </table></center>
        '''
    )

def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    #newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount', 'off')
    #print(removepunc) #it's checking words on ur terminal
    #print(djtext)
    if removepunc == "on":
        punctuations='''!@#$%^&*()_{}[]:;""''?/<>.,~`\|-~+='''
        input = ""
        for char in djtext:
            if char not in punctuations:
                input = input + char
        param = {'purpose': '.....', 'analyzed_text': input}
        djtext = input
        #return render(request, 'analyze.html', param)
    if (fullcaps=="on"):
        input=''
        for char in djtext:
            input=input+char.upper()

        param={'purpose':'.....','analyzed_text':input}
        djtext = input
        #return render(request,'analyze.html',param)
   # if (newlineremover=="on"):
   #     input=''
   #     for char in djtext:
   #         if char != "\n":
   #             input = input + char

   #     param = {'purpose': 'Removed NewLines', 'analyzed_text': input}
         #djtext = input
   #     #return render(request, 'analyze.html', param)
   # in this case we have to remove textarea form from analyze.html to see proper result

    if(extraspaceremover=="on"):
        input=''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                input=input+char
        param = {'purpose': '.....', 'analyzed_text': input}
        djtext = input

    #if(charcount=='on'):
    #    input=0
    #    for char in djtext:
    #        if(char != ' '):
    #            input=input+1
    #    param = {'purpose': '.....', 'analyzed_text': input}
    #    djtext = input
    #    #return render(request, 'analyze.html', param)


    if(removepunc != "on" and fullcaps!="on" and extraspaceremover!="on"):
        return HttpResponse("<style>body{background-color:lightgreen;text-align:center;padding-top:10;margin-top:100;}</style><h1 style=color:red;>ERROR:Please select operation !!!</h1>")
    else:
        return render(request, 'analyze.html', param)



