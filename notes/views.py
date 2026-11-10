
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note, Category
from .forms import NoteForm
from django.db.models import Count, Q

# Create your views here.

@login_required
def notes_list(request):
    notes = Note.objects.filter(
        user=request.user
    ).order_by('-created_at')

    categories = Category.objects.all()

    selected_category_id = request.GET.get('category')

    if selected_category_id and selected_category_id.isdigit():
        selected_category_id = int(selected_category_id)
        notes = notes.filter(category_id=selected_category_id)
    else:
        selected_category_id = None

    category_counts = Category.objects.annotate(
        notes_count=Count(
            'note',
            filter=Q(note__user=request.user)
        )
    )

    return render(request, 'notes/notes_list.html', {
        'notes': notes,
        'categories': categories,
        'selected_category_id': selected_category_id,
        'category_counts': category_counts
    })


@login_required
def create_note(request):

    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            Note.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                category=form.cleaned_data['category'],
                user=request.user
            )

            return redirect('notes_list')

    else:
        form = NoteForm()

    return render(request, 'notes/create_note.html', {
        'form': form
    })


@login_required
def note_detail(request, note_id):
    note = get_object_or_404(
        Note,
        id=note_id,
        user=request.user
    )

    return render(request, 'notes/note_detail.html', {
        'note': note
    })

@login_required
def delete_note(request, note_id):

    if request.method == 'POST':
        note = get_object_or_404(
            Note,
            id=note_id,
            user=request.user
        )

        note.delete()

    return redirect('notes_list')