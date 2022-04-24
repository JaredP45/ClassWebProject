from django.db import models


class UpperSection(models.Model):
    banner = models.ImageField(blank=True)
    welcome_message = models.CharField(max_length=250)

    def __str__(self):
        return "Welcome Banner and Text"


class MidSection(models.Model):
    about_us = models.TextField(default='Enter text about us.', blank=True)

    def __str__(self):
        return "About Us"


class StudentSection(models.Model):
    student_section_description = models.TextField(max_length=750, default="")

    def __str__(self):
        return "Student Section Description"


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
        return "Footer"
