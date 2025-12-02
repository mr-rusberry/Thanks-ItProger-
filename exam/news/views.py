from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def news_main(request):
    news = Articles.objects.order_by("-date")
    return render(request, 'news/news_main.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'articles'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/add_news.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news_delete.html'
    success_url = '/news/'


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
