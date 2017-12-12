from libraries.django_rest_admin.register import rest_admin
from .models import *

rest_admin.register(DemoMessage)