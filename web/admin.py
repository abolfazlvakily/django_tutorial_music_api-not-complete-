from django.contrib import admin
from  .models import (Artist,Album,Tag,Track,)


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Tag)
