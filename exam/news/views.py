from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


# Create your views here.
def news_main(request):
    news = Articles.objects.order_by("-date")
    return render(request, 'news/news_main.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'articles'


def add_news(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = "Form incorrect"

    form = ArticlesForm()
    return render(request, 'news/add_news.html', {'form': form, 'error': error})
