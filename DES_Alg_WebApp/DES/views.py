from django.shortcuts import render
from django.http import HttpResponse
from .des_function import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,'DES/index.html')
@csrf_exempt
def encrypt(request):
    if request.method == "POST":
        message = str(request.POST.get('plain_text'))
        Key =str(request.POST.get('Key'))
        Key = hex2bin(Key)
        cipher_text = encryption(message, Key)
        return HttpResponse(bin2hex(cipher_text))
    return HttpResponse("Illegal Request")


@csrf_exempt
def decrypt(request):
    if request.method == "POST":
        cipher = str(request.POST.get('cipher_text'))
        cipher = hex2bin(cipher)
        Key =str(request.POST.get('Key'))
        Key = hex2bin(Key)
        return HttpResponse(process(bin2string(decryption(cipher, Key))))
    return HttpResponse("Illegal Request")
