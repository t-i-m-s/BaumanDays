from django.db import models
import os
from BaumanDays import settings


def images_path():
    return os.path.join(settings.BASE_DIR, '/static/src/pic/teacher_pic')
# Create your models here.
class TeacherRating(models.Model):
	"""docstring for ClassName"""
	name = models.CharField('name', max_length = 50)
	surname = models.CharField('surname', max_length = 50)
	patronymic = models.CharField('patronymic', max_length = 50)
	discipline = models.CharField('discipline', max_length = 50)
	knowledge_level = models.IntegerField('knowledge level')
	character_level = models.IntegerField('character level')
	photo_path = models.ImageField(blank=True)
	discipline_photo_path = models.ImageField(blank=True)
    # verbose_name='discipline photo',
    #                                 upload_to='discipline_photo/',
    #                                 max_length=256,
	description = models.TextField('description')

	def __str__(self):
		return self.name
	def get_discipline(self):
		return self.discipline
	def get_photo_path(self):
		return self.photo_path


class Comment(models.Model):
	teacher = models.ForeignKey(TeacherRating, on_delete = models.CASCADE)
	author_name = models.CharField('author name', max_length = 50)
	comment_text = models.CharField('comment text', max_length = 500)

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
