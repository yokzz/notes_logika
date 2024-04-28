from django.shortcuts import render, redirect
from notes.models import Note
from django.views.generic import ListView, DetailView
from notes.forms import NoteForm


class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "note_list.html"
    

class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template = "note_detail.html"
    
def note_form(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = NoteForm()
    
    return render(request,
                  'notes/note_form.html',
                  {"form": form}
            )

