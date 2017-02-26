#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EnWord(models.Model):
	word = models.CharField(max_length = 64, unique = True)
	en_explanation = models.CharField(verbose_name = u'Англи тайлбар',max_length = 512)
	mn_explanation = models.CharField(verbose_name = u'Монгол тайлбар', max_length = 512)
	en_us_pronunciation = models.CharField(verbose_name = u'Америк дуудлага', max_length = 64)
	en_br_pronunciation = models.CharField(verbose_name = u'Америк дуудлага', max_length = 64)
	synonyms = models.ForeignKey('self', related_name = 'syns')
	antonyms = models.ForeignKey('self', related_name = 'antos')

class EnExampleSentence(models.Model):
	sentence = models.CharField(verbose_name = u'Жишээ өгүүлбэр', max_length = 512)
	en_words = models.ManyToManyField(EnWord)

class EnWordDefinition(models.Model):
	word = models.ForeignKey(EnWord)
	en_definition = models.CharField(verbose_name = u'Англи тодорхойлолт', max_length = 512)
	mn_definition = models.CharField(verbose_name = u'Монгол тодорхойлолт', max_length = 512)
	# tag baih heregtei baij magadgui
