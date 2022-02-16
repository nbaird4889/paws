from django.contrib import admin
from .models import Dog, Visitors, Photo, Walker

# Register your models here.
admin.site.register(Dog)
admin.site.register(Visitors)
admin.site.register(Photo)
admin.site.register(Walker)
