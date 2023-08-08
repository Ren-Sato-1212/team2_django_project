from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    photo_path = models.CharField(max_length=255)

    def __str__(self):
        return f'[{self.pk}] {self.name}'

class Career(models.Model):
    member_pk = models.ForeignKey(Member, on_delete=models.CASCADE)
    career = models.TextField()
    
    def __str__(self):
        return f'[{self.member_pk}] {self.pk}'

class ContactCategory(models.Model):
    name = models.CharField(max_length=30)
    icon_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Contact(models.Model):
    member_pk = models.ForeignKey(Member, on_delete=models.CASCADE)
    category = models.ForeignKey(ContactCategory, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f'[{self.member_pk}] {self.category}'

class SkillCategory(models.Model):
    name = models.CharField(max_length=30)
    icon_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Skill(models.Model):
    member_pk = models.ForeignKey(Member, on_delete=models.CASCADE)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.member_pk}] {self.category}'

class Portfolio(models.Model):
    member_pk = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo_path = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return f'[{self.member_pk}] {self.title}'

class Hobby(models.Model):
    member_pk = models.ForeignKey(Member, models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo_path = models.CharField(max_length=255)

    def __str__(self):
        return f'[{self.member_pk}] {self.title}'