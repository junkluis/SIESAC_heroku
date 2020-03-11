from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from datetime import datetime
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from django.conf import settings
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from random import  randrange
import qrcode
import smtplib
import mimetypes
import json
import os, smtplib

	