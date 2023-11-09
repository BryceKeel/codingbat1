from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.
def near_hundred(request: HttpRequest,n: int) -> HttpResponse:
  if (abs(100 - n) <= 10) or (abs(200 - n) <= 10):
    return HttpResponse(True)
  else:
    return HttpResponse(False)

def string_splosion(request: HttpRequest,str: str) -> HttpResponse:
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return HttpResponse(result)

def cat_dog(request: HttpRequest,cd: str) -> HttpResponse:
  cats = 0
  dogs = 0
  for x in range(len(cd) - 1):
    if cd[x: x + 3] == "cat":
      cats+=1
    elif cd[x: x + 3] == "dog":
      dogs+=1
  return HttpResponse(cats == dogs)

def lone_sum(request: HttpRequest,a: int,b: int,c: int) -> HttpResponse:
  sum = 0
  if a != b and a != c:
    sum+=a
  if b != a and b != c:
    sum+=b
  if c != a and c != b:
    sum+=c
  return HttpResponse(sum)
