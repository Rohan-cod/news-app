from django.core.management.base import BaseCommand
from newsapi import NewsApiClient
from news.models import News

class Command(BaseCommand):
	help = "collect top headlines from newsapi"
	def handle(self, *args, **options):
		newsapi = NewsApiClient(api_key='3f8e6fbc9b2a45379023c71f61ec354a')
		top_headlines = newsapi.get_top_headlines(language='en', country='in')
		if top_headlines['status'] == "ok":
			for article in top_headlines['articles']:
				title = article['title']
				author = article['author']
				source = article['source']['name']
				description = article['description']
				url = str(article['url'])
				url_to_image = str(article['urlToImage'])
				published_at = article['publishedAt']
				content = article['content']
				try:
					News.objects.create(
							title=title,
							author=author,
							url=url,
							source=source,
							desciption=description,
							url_to_image=url_to_image,
							published_at=published_at,
							content=content
						)
				except:
					pass




