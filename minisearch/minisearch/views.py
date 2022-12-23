import csv

from django.shortcuts import render
from .settings import DATASET_FILE
import Levenshtein as lev



def index(request):
  with open(DATASET_FILE) as dataset_file:
    csv_data = csv.reader(dataset_file, delimiter=',')
    values = []
    for i, row in enumerate(csv_data):
      if i == 0: continue
      values.append(row[0])

  return render(request, 'index.html', {"values": values})

def search(request):
  q = request.GET.get('key')
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

    for i, row in enumerate(csv_data):
      if i == 0: continue
      ratio = lev.ratio(search_value.lower(), row[1].lower())

      if ratio >= 0.5:
        results[row[1]] = round(100 * ratio, 2)

  return render(request, 'result.html', {'q': q, 'results': results})
