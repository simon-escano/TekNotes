from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    COLORS = [
        ('red-500', 'Red'),
        ('orange-500', 'Orange'),
        ('amber-500', 'Amber'),
        ('lime-500', 'Lime'),
        ('green-500', 'Green'),
        ('emerald-500', 'Emerald'),
        ('teal-500', 'Teal'),
        ('cyan-500', 'Cyan'),
        ('blue-500', 'Blue'),
        ('indigo-500', 'Indigo'),
        ('violet-500', 'Violet'),
        ('purple-500', 'Purple'),
        ('fuschia-500', 'Fuschia'),
        ('pink-500', 'Pink'),
    ]

    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=20, choices=COLORS, default='gray-500')

    def __str__(self):
        return f'{self.code} - {self.description}'
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)
    tags = models.ManyToManyField(Tag, related_name='notes', blank=True)

    def __str__(self):
        return self.title
    
class Element(models.Model):
    note = models.ForeignKey(Note, related_name='elements', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']
        unique_together = ['note', 'order']

    def __str__(self):
        return f'Element {self.order} of Note: {self.note.title}'
    
class TextElement(Element):
    content = models.TextField()

class FileElement(Element):
    file_url = models.URLField(default='')
