from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import TeacherRating
import os
from BaumanDays import settings


# Create your views here.
def disciplines_list(request):
	latest_teachers_list = TeacherRating.objects.all()
	disciplines = set(map(lambda x: x.get_discipline(), latest_teachers_list))
	return render(request, 'disciplines_list.html', context={
		'latest_teachers_list': latest_teachers_list,
		'disciplines' : disciplines
		})


def teachers_list(request, discipline):
	teachers_list = TeacherRating.objects.filter(discipline = discipline)
	return render(request, 'teachers_list.html', context={
		'teachers_list': teachers_list,
		'discipline': discipline,
		})

def teacher(request, teacher):
	#os.path.relpath('/mnt/d/python/django/baumandays/static/src/pic/teacher_pic/default_teacher_pic.jpg',
	#start = settings.STATIC_IMAGES_PATH)
	teacher = TeacherRating.objects.filter(id = teacher)
	return HttpResponse(teacher[0].photo_path)
