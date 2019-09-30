'''
    Przykładowy plik `urls.py`
'''
from django.conf.urls import url
from myapp.views import HomePage, ShowTags, ShowPagesForTag, ShowPage


urlpatterns = [
    # Strona główna - `HomePage` jest prostą funkcją
    url(r'^$',                          HomePage ,                   name='HomePage'),

    # Strona z wylistowaniem tagów - `ShowTags` jest klasą
    url(r'^tag/$',                      ShowTags.as_view(),          name='ShowTags'),

    # Wyświtlanie stron - `ShowPage` jest klasą
    # - `(?P<slug>[a-z]+)\.html` -  pozwala wyłuskać z adresów takich jak np. `about.html`
    #   część udającą nazwę pliku, bez rozszeżenia `.html`
    url(r'^(?P<slug>[a-z]+)\.html$',    ShowPage.as_view(),          name='ShowPage'),

    # Wyślitlenie wszystkich stron z danym tagiem - `ShowPagesForTag` jest klasą
    # - `tag-(?P<tag>[a-z]+)/` - pasuje do np. `tag-info` lub `tag-company`
    url(r'^tag-(?P<tag>[a-z]+)/$',      ShowPagesForTag.as_view(),   name='ShowPagesForTag')
]
