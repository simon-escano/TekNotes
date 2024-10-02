from django.shortcuts import render, redirect
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

def your_notes(request):
    notes = Note.objects.filter(created_by=request.user)
    courses = Course.objects.filter(note__in=notes).distinct()
    tags = Tag.objects.filter(notes__in=notes).distinct()

    return render(request, 'core/your_notes.html', {
        'notes': notes,
        'courses': courses,
        'tags': tags
    })

def likes(request):
    notes = Note.objects.filter(likes=request.user).distinct()
    courses = Course.objects.filter(note__in=notes).distinct()
    tags = Tag.objects.filter(notes__in=notes).distinct()

    return render(request, 'core/likes.html', {
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

def login(request):
    pass
    

def logout(request):
    return redirect('/signup/')