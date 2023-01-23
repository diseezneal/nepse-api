from rest_framework.views import APIView
from rest_framework.response import Response

from scraper.core import NepseScraper


class ScrapeView(APIView):
    def post(self, request, format=None):
        NepseScraper().run_scraper()

        return Response({'message': 'success'})
