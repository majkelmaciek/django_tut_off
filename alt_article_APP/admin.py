from django.contrib import admin

from alt_article_APP.models import Question, Choice

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)