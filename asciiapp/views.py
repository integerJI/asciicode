from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def encryption(request):

    full_text = request.GET['fulltext']
    list_text = list(map(str,full_text))
    dic_text = []

    for i in list_text:
        ascii_text = hex(ord(i)).replace("0x","")
        dic_text.append(ascii_text)

    return render(request, 'encryption.html', { 'ascii': dic_text } )
