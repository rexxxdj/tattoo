# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Services(models.Model):
	''' Service Model '''
	class Meta(object):
		verbose_name=u'Услуга'
		verbose_name_plural=u'Услуги'

	name = models.CharField(
		max_length=255,
		blank=False,
		verbose_name = u'Название')

	small_desc = models.CharField(
		max_length=255,
		blank=False,
		verbose_name=u'Краткое описание')

	description = models.TextField(
		blank=True,
		verbose_name='Полное описание')

	image = models.ImageField(
		upload_to='img/services/',
		verbose_name = u'Фото',
		blank=True,
		null=True)

	def __unicode__(self):
		return u'%s' % (self.name)