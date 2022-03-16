from django.db import models


class UpperSection(models.Model):
    banner = models.ImageField(blank=True)
    welcome_message = models.CharField(max_length=250)

    def __str__(self):
        return self.welcome_message


class MidSection(models.Model):
    game_photo = models.ImageField(blank=True)
    movie_photo = models.ImageField(blank=True)
    about_us = models.TextField(default='Enter text about us.', blank=True)

    def __str__(self):
        return "About us"


class LowerSection(models.Model):
    member_photo = models.ImageField(blank=True)
    member_name = models.CharField(max_length=250, default="")
    member_major = models.CharField(max_length=250, default="")
    member_desc = models.TextField(max_length=750, default="")
    member_contact = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.member_name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class PageFooter(models.Model):
    info = models.CharField(max_length=250)

    def __str__(self):
        return self.info
