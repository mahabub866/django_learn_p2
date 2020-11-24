from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic import(
CreateView,
DeleteView,
ListView,
UpdateView,
DetailView

)
from .forms import ArticleModelForm

from .models import Article
# Create your views here.
class ArticleListView(ListView):
    template_name = 'article/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'article/article-detail.html'
    queryset = Article.objects.all()

class ArticleCreateView(CreateView):
    template_name = 'article/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all() # <blog>/<modelname>_list.html
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = 'article/article_create.html'
    form_class = ArticleModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'article/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('article:article-list')