# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from django.utils import timezone

# Create your views here.
class IndexView(generic.TemplateView):
	"""docstring for IndexView"""
	template_name = 'home/index.html'

