from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Member)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(WantToRead)
admin.site.register(Stacks)
