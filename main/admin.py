from django.contrib import admin

from .models import Member, Career, ContactCategory, Contact, SkillCategory, Skill, Portfolio, Hobby

admin.site.register(Member)
admin.site.register(Career)
admin.site.register(ContactCategory)
admin.site.register(Contact)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(Portfolio)
admin.site.register(Hobby)
