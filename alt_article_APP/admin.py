from django.contrib import admin

from alt_article_APP.models import  Question, Choice, Domena_WWW, Alt_url_link, Alt_article

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Domena_WWW)
admin.site.register(Alt_url_link)
admin.site.register(Alt_article)