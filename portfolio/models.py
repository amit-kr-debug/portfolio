from django.db import models


class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = 'portfolio/images/')
    github_url = models.URLField(blank = True)
    live_url = models.URLField(blank = True)

    def __str__(self):
        return self.title


class Education(models.Model):
    institute = models.CharField(max_length = 100)
    board_of_education = models.CharField(max_length = 100)
    degree = models.CharField(max_length = 100)
    year_of_completion = models.IntegerField()
    score = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.institute


class Experience(models.Model):
    company = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField(null= True, blank = True)
    role = models.CharField(max_length = 100)

    def __str__(self):
        return self.company


class SkillsAndTool(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'portfolio/images/')