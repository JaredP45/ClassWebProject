from django.contrib import admin

from .models import UpperSection, MidSection, LowerSection, PageFooter, StudentSection

admin.site.register(UpperSection)
admin.site.register(MidSection)
admin.site.register(StudentSection)
admin.site.register(LowerSection)
admin.site.register(PageFooter)
