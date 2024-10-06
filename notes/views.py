from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404  
from .forms import NoteForm
from tags.models import Tag
from .models import Note

def tek_a_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user

            note.save()
            
            tag_input = request.POST.get('tags', '')
            if tag_input:
                tag_names = [tag.strip() for tag in tag_input.split(',')]
                for tag_name in tag_names:
                    if tag_name:
                        tag, created = Tag.objects.get_or_create(name=tag_name)  
                        note.tags.add(tag)

            return redirect('/your_notes/')
    else:
        form = NoteForm()

    return render(request, 'notes/tek_a_note.html', {'form': form})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, created_by=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('/your_notes/')
    
    return redirect("/your_notes/")

@login_required
def archive_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, created_by=request.user)
    
    if request.method == 'POST':
        note.is_archived = not note.is_archived
        note.save()
        return redirect('/archive/')
    
    return redirect("/archive/")