from django.db import models


class UpperSection(models.Model):
    banner = models.ImageField(blank=True)
    welcome_message = models.CharField(max_length=250)

    def __str__(self):
        return "Welcome banner"

    class Meta:
        verbose_name = 'Upper Section'
        verbose_name_plural = 'Upper Sections'


class MidSection(models.Model):
    game_photo = models.ImageField(blank=True)
    movie_photo = models.ImageField(blank=True)
    about_us = models.TextField(default='Enter text about us.', blank=True)

    def __str__(self):
        return "About us"

    class Meta:
        verbose_name = 'Middle Section'
        verbose_name_plural = 'Middle Sections'


class LowerSection(models.Model):
    MAJOR = (
        (0, "Web Development"),
        (1, "Software Development"),
        (2, "Digital Media"),
    )

    member_photo = models.ImageField(blank=True)
    member_name = models.CharField(max_length=250, default="")
    member_major = models.IntegerField(choices=MAJOR, default=0)
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

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footers'
