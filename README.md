# PPP_Django
czyli `Prosty Przykładowy Projekt w Django`

na potrzeby zajęć z Modułu 3

---
Przykładowe dane najprościej wstawić wywołując polecenie:

```python manage.py shell```

oczywiście znajdując się w katalogu projektu i venvie :) No i już po migracji ;)

Następnie można:
```
# zaimportować modele
from myapp.models import WebPage, Tag  
# Utworzyć kilka stron, tak:
about = WebPage()
about.title = 'About US'               
about.content = 'Our company is just THE BEST!'                    
about.slug = 'about'                   
about.save()                           
# lub tak:
team = WebPage.objects.create(title='Our TEAM',content='Our team contains THE BEST peaople!',slug='team')
contact = WebPage.objects.create(title='Contact',content='If You need to contact Us send an e-mail!',slug='contact')
# Utworzyć klika tagów:
company_tag = Tag.objects.create(name='company')                  
info_tag = Tag.objects.create(name='info')                        
peaople_tag = Tag.objects.create(name='peaople')                  
# Dodać strony do tagów:
company_tag.pages.add(about)          
company_tag.pages.add(contact)        
# albo ustawić strony dla tagów:
info_tag.pages.set( (about,team) )    
# Lub od drugiej strony - dodać tagi do stron:
team.tag_set.add(peaople_tag)   
```
