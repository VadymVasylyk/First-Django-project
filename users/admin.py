from django.contrib import admin
from .models import Profile
from .models import Messages

admin.site.register(Profile)
admin.site.register(Messages)

