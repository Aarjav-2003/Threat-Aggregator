import csv
import os
from django.shortcuts import render

def ioc_list(request):
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'parsed_feeds', 'aggregated_iocs.csv')
    
    iocs = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            iocs.append(row)

    return render(request, 'dashboard/ioc_list.html', {'iocs': iocs})
