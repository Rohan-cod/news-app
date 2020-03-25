from django.views.generic import ListView, TemplateView, DetailView
from .models import News 
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render



class NewsListView(ListView):
	model = News
	template_name = 'news.html'
	paginate_by = 5
	ordering = ['-published_at']

class HomePageView(TemplateView):
	template_name = 'index.html'

class NewsDetailView(DetailView):
	model = News
	template_name = 'news_detail.html'
	login_url = 'login'

def search_view(request):
	ctx = {}
	url_parameter = request.GET.get("q")

	if url_parameter:
		news = News.objects.filter(source__icontains=url_parameter)
	else:
		news = News.objects.all()

	ctx["news"] = news

	if request.is_ajax():
		html = render_to_string(
			template_name="news-results-partial.html", 
			context={"news": news}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request, "news_search.html", context=ctx)





