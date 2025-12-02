from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


# Create your views here.
def news_main(request):
    news = Articles.objects.order_by("-date")
    return render(request, 'news/news_main.html', {'news': news})

def add_news(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = "Form encorrect"


    form = ArticlesForm()
    return render(request, 'news/add_news.html', {'form': form, 'error': error})
