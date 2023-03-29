from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'first_name')

@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'is_key_skill')

@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
	list_display = ('id', 'institution', 'date', 'is_active')

@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
	list_display = ('id', 'company', 'date', 'is_active')

@admin.register(models.Certificate)
class CertificateAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

@admin.register(models.CodingProfiles)
class CodingProfilesAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

@admin.register(models.CertificateImages)
class CertificateImagesAdmin(admin.ModelAdmin):
	list_display = ('id',)

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('id', 'title')

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):	
	list_display = ('id', 'name')