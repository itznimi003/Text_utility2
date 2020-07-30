#I have created this file-"nimi"
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    #Check checkbox values
    removepunc = request.POST.get('removepunc', 'off') 
    fullcaps = request.POST.get('fullcaps', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')  
    #check which checkbox is on
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations','analyzed_text': analyzed }
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    # return HttpResponse("<a href='https://www.google.com/'>Google</a>")
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed  = analyzed + char.upper()
            params = {'purpose': 'changed to uppercase','analyzed_text': analyzed }
            djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed  = analyzed + char
        params = {'purpose': 'remove new lines','analyzed_text': analyzed }
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed  = analyzed + char
        params = {'purpose': 'extraspaceremover','analyzed_text': analyzed }
        djtext = analyzed
     
    return render(request, 'analyze.html', params)   