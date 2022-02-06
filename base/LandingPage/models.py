from django.db import models


class Navbar(models.Model):
    page = models.CharField(max_length=250)

    def __str__(self):
        return self.page


class UpperSection(models.Model):
    banner = models.ImageField(blank=True)
    welcome_message = models.CharField(max_length=250)

    def __str__(self):
        return self.welcome_message


class MidSection(models.Model):
    about_us = models.CharField(max_length=250)

    def __str__(self):
        return self.about_us


class LowerSection(models.Model):
    """
        Image grid will house every classmate and their personalized page.
        This is currently a placeholder.
    """
    member_photo = models.ImageField(blank=True)

    def __str__(self):
        return self.member_photo


class PageFooter(models.Model):
    info = models.CharField(max_length=250)

    def __str__(self):
        return self.info
