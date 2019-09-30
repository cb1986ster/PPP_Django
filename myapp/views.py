from django.shortcuts import render
from django.views import View
from .models import WebPage, Tag

def HomePage(request):
    return render(request,'HomePage.html')

class ShowPage(View):
    def get(self, request, slug):
        page = WebPage.objects.get(slug=slug) # Tu może pojawić się wyjątek !
        return render(request, 'ShowPage.html', {'page':page})

class ShowTags(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request,'ShowTags.html',{'tags':tags})

class ShowPagesForTag(View):
    def get(self, request, tag):
        tag = Tag.objects.get(name=tag) # Tu może pojawić się wyjątek !
        return render(request,'ShowPagesForTag.html',{'tag':tag})
