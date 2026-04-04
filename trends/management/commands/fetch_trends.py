from django.core.management.base import BaseCommand
from trends.models import Trend
from datetime import date
import requests

class Command(BaseCommand):
    help = "Fetch trending topics and save to database"

    def handle(self, *args, **kwargs):
        self.stdout.write("Fetching trends...")

        url = "https://trends.google.com/trends/api/dailytrends?hl=en-US&geo=IN"

        response = requests.get(url)
        data = response.text

        # Google sends weird JSON with extra characters
        clean_json = data.replace(")]}',", "")
        import json
        trends_data = json.loads(clean_json)

        today_trends = trends_data["default"]["trendingSearchesDays"][0]["trendingSearches"]

        for trend in today_trends:
            title = trend["title"]["query"]
            traffic = trend["formattedTraffic"]

            Trend.objects.create(
                title=title,
                traffic=traffic,
                date=date.today()
            )

            self.stdout.write(self.style.SUCCESS(f"Saved: {title}"))

        self.stdout.write(self.style.SUCCESS("All trends saved 🎉"))