import csv

from django.shortcuts import render
from .settings import DATASET_FILE
import Levenshtein as lev
from django.http import HttpResponseBadRequest, HttpResponseNotFound

from django_ratelimit.decorators import ratelimit


@ratelimit(key='ip', rate='5/m')
def index(request):
  with open(DATASET_FILE) as dataset_file:
    csv_data = csv.reader(dataset_file, delimiter=',')
    values = []
    for i, row in enumerate(csv_data):
      if i == 0: continue
      values.append(row[0])

  return render(request, 'index.html', {"values": values})


@ratelimit(key='ip', rate='5/m')
def search(request):
  q = request.GET.get('key')
  if not q:
    return HttpResponseBadRequest()

  results = dict()
  search_value = None

  with open(DATASET_FILE) as dataset_file:
    csv_data = list(csv.reader(dataset_file, delimiter=','))
    for i, row in enumerate(csv_data):
      if i == 0: continue
      if row[0] == q:
        search_value = row[1]
        print(f"Got search value {search_value}")
        break

    if not search_value:
      return HttpResponseNotFound()

    for i, row in enumerate(csv_data):
      if i == 0: continue
      ratio = lev.ratio(search_value.lower(), row[1].lower())

      if ratio >= 0.5:
        results[row[1]] = round(100 * ratio, 2)

  return render(request, 'result.html', {'q': q, 'results': results})
