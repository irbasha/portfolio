from django.contrib import admin
from core.models import Person, Profile, Skills, Experience, Education, Projects


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0

class SkillsInline(admin.StackedInline):
    model = Skills
    extra = 0

class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 0

class EducationInline(admin.StackedInline):
    model = Education
    extra = 0

class ProjectInline(admin.StackedInline):
    model = Projects
    extra = 0

class PersonAdmin(admin.ModelAdmin):
    inlines = [ProfileInline, SkillsInline, ExperienceInline, EducationInline, ProjectInline]

admin.site.register(Person, PersonAdmin)
