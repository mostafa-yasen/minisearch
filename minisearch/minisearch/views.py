from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def search(request):
  q = request.GET.get('q')
  # TODO: implement search method.
  return render(request, 'result.html', {'q': q})
