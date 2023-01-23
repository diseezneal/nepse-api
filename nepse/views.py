import csv
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


class TodaysPrice(APIView):
    def get(self, request, format=None):
        res = []

        with open(settings.BASE_DIR / 'data/todaysprice.csv', 'r', encoding='UTF-8') as csvf:
            csvReader = csv.DictReader(csvf)

            for row in csvReader:
                res.append(row)

        return Response(res)
