from django.http import HttpResponse
def test(request):
    return HttpResponse("<h>hello world</h1")