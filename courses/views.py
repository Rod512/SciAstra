from django.shortcuts import render
from .models import Course
from django.utils.timezone import now


def home(request):
     
    discounted_courses = Course.objects.filter(discount__gt=0)
    context = {
        'discounted_courses': discounted_courses,
        'version': now().timestamp(),
    }
    return render(request, 'courses/home.html', context)

