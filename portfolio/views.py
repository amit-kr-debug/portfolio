from django.shortcuts import render
from .models import Project, Education, Experience, SkillsAndTool


def home(requests):
    projects = Project.objects.all()
    educations = Education.objects.order_by('-year_of_completion')
    experiences = Experience.objects.all()
    skillsAndTools = SkillsAndTool.objects.all()
    return render(requests, 'portfolio/home.html', {'projects': projects,
                                                    'educations': educations,
                                                    'experiences': experiences,
                                                    'skillsAndTools': skillsAndTools})
