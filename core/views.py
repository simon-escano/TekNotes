from django.shortcuts import render, redirect
from django.contrib.auth import logout as log_out
from django.db.models import Q
from note.models import Note, Course, Tag
from .forms import SignupForm

def index(request):
    notes = Note.objects.all()
    courses = Course.objects.filter(note__in=notes).distinct()
    tags = Tag.objects.filter(notes__in=notes).distinct()

    return render(request, 'core/index.html', {
        'notes': notes,
        'courses': courses,
        'tags': tags
    })

def search(request):
    query = request.GET.get('query', '')
    if query:
        notes = Note.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) |
            Q(tags__name__icontains=query) |
            Q(course__description__icontains=query) |
            Q(created_by__username__icontains=query) |
            Q(created_by__first_name__icontains=query) |
            Q(created_by__last_name__icontains=query)
        ).distinct()
    else:
        notes = Note.objects.all()

    return render(request, 'core/index.html', {
        'notes': notes,
        'query': query,
    })


def your_notes(request):
    notes = Note.objects.filter(created_by=request.user)
    courses = Course.objects.filter(note__in=notes).distinct()
    tags = Tag.objects.filter(notes__in=notes).distinct()

    return render(request, 'core/index.html', {
        'notes': notes,
        'courses': courses,
        'tags': tags
    })

def likes(request):
    notes = Note.objects.filter(likes=request.user).distinct()
    courses = Course.objects.filter(note__in=notes).distinct()
    tags = Tag.objects.filter(notes__in=notes).distinct()

    return render(request, 'core/index.html', {
        'notes': notes,
        'courses': courses,
        'tags': tags
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


def logout(request):
    log_out(request)
    return redirect('/')