from django.conf import settings
from django.contrib import admin

from .models import UpperSection, MidSection, LowerSection, PageFooter, StudentSection


class SectionAdmin(admin.ModelAdmin):
    if not settings.DEBUG:
        def has_delete_permission(self, request, obj=None):
            return False

        def has_add_permission(self, request):
            return False


admin.site.register(UpperSection, SectionAdmin)
admin.site.register(MidSection, SectionAdmin)
admin.site.register(StudentSection, SectionAdmin)
admin.site.register(LowerSection)
admin.site.register(PageFooter, SectionAdmin)
