# -*- encoding: utf-8 -*-
from djongo import models
import simplejson
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.translation import activate

from rest_framework import views, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.conf import settings

from django.contrib.auth.decorators import login_required
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from camaras.forms import CamarasForm
from camaras.models import Camaras
from aforoInfo.models import AforoInfo
from monitor.models import Monitor
from django.forms.models import model_to_dict
from django.core import serializers


# Create your views here.



