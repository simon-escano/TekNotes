from django.contrib import admin
from .models import Course, Tag, Note, Element, TextElement, FileElement

admin.site.register(Course)
admin.site.register(Tag)
admin.site.register(Note)
admin.site.register(Element)
admin.site.register(TextElement)
admin.site.register(FileElement)