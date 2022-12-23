import csv

from django.shortcuts import render
from .settings import DATASET_FILE
import Levenshtein as lev
from django.http import HttpResponseBadRequest, HttpResponseNotFound

from django_ratelimit.decorators import ratelimit


# Limit requests to 5 requests per minute.
@ratelimit(key='ip', rate='5/m')
def index(request):
  """Handles the '/' route"""
  # Open the dataset to get the select options
  with open(DATASET_FILE) as dataset_file:
    # Read data from csv file
    csv_data = csv.reader(dataset_file, delimiter=',')

    # Prepare the output list
    values = []
    for i, row in enumerate(csv_data):
      # Skip the header row
      if i == 0: continue

      # Append the value to the output
      values.append(row[0])

  # Return values to be rendered in the template.
  return render(request, 'index.html', {"values": values})


@ratelimit(key='ip', rate='5/m')
def search(request):
  # Get query string parameter
  q = request.GET.get('key')

  # Validate that the key exists
  if not q: return HttpResponseBadRequest()

  # Prepare the output dict
  results = dict()
  
  # Prepare the search value
  search_value = None

  # Open dataset file to search
  with open(DATASET_FILE) as dataset_file:
    # Load data from csv file
    csv_data = list(csv.reader(dataset_file, delimiter=','))

    # Flag indicates if the key found or not
    key_found = False

    # Loop to get the search value of the given key
    for i, row in enumerate(csv_data):
      # Skip headers row
      if i == 0: continue

      # If the key matches the given key, break.
      if row[0] == q:
        key_found = True
        search_value = row[1]
        break

    # Make sure the key exists in the dataset file
    if not key_found: return HttpResponseNotFound()

    # Loop over the list to get the matching rates
    for i, row in enumerate(csv_data):
      # Skip headers row
      if i == 0: continue

      # Get the matching rate
      ratio = lev.ratio(search_value.lower(), row[1].lower())

      # Exclude the item itself
      if ratio == 1: continue

      # Include the matches above 50%
      if ratio >= 0.5:
        results[row[1]] = round(100 * ratio, 2)

  # Return the data to be rendered
  return render(request, 'result.html', {'q': q, 'results': results})
