import datetime

from django.db import models
from django.utils import timezone

# Create your models here.



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Tag(models.Model):
    name = models.CharField(max_length=30)

class Domena_WWW(models.Model):
    URL = models.URLField()
    rating = models.IntegerField(default=0)
    catergory = models.CharField(max_length=100)    # strony polityczne: lewa, prawa, centro, tech, culture, plotki, news, finanse, itd, podobnie jak w newsvoice
    summary = models.TextField()

class Alt_url_link(models.Model):
    URL = models.URLField()
    rating = models.IntegerField(default=0)
    domena_WWW = models.ForeignKey(Domena_WWW, on_delete=models.SET_NULL, null=True)   # każda domena serwis WWW powienien też być klasą  (A nie tylko models.URLField()), bo powienien miec swoja ocenę, link, atrybuty(jaki serwis), komentarze itd
    
class Alt_article(models.Model):
    title = models.CharField(max_length=200)
    alt_url_link = models.ForeignKey(Alt_url_link, on_delete=models.SET_NULL, null=True)     # alt_url_link - tez powienine byc klasa (A nie tylko models.URLField()), bo powienien miec swoja ocenę, link, zrodlo, atrybuty(jaki serwis/domena), komentarze itd, ocena domeny też ma wpływ na ocenę alt_link
    summary = models.TextField()
    pub_date = models.DateTimeField('date published')
    tag = models.ManyToManyField(Tag)