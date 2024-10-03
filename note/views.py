from django.shortcuts import render, redirect
from .forms import NoteForm

def new_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user
            note.save()
            form.save_m2m()
            return redirect('/your_notes/')
    else:
        form = NoteForm()

    return render(request, 'note/new_note.html', {'form': form})