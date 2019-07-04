from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to="profile_pics")
    def __str__(self):
        return f"{self.user.username} 's Profile"

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class TutorialCategory(models.Model):

    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published',default=datetime.now())
    #https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.tutorial_title

class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_content = models.TextField()
    news_published = models.DateTimeField('date published',default=datetime.now())
    #https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    # tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    # tutorial_slug = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.news_title

class TournamentCategory(models.Model):
    tournament_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tournament_category

class TournamentSeries(models.Model):
    tournament_series = models.CharField(max_length=200)
    tournament_category = models.ForeignKey(TournamentCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "tournament Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tournament_series

class Tournament(models.Model):
    tournament_title = models.CharField(max_length=200)
    tournament_content = models.TextField()
    tournament_published = models.DateTimeField('date published',default=datetime.now())
    #https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    tournament_series = models.ForeignKey(TournamentSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tournament_slug = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.tournament_title
