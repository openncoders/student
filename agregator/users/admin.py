
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Teacher


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('study_direction',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('study_direction',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'difficulty')
    list_filter = ('difficulty',)
    search_fields = ('name', 'surname')
