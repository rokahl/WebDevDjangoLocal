from django.shortcuts import render, redirect
from .models import ToDoItem
from .forms import ToDoItemForm  # Make sure to create a forms.py file in your app

def todo_list(request):
    # Hole alle ToDoItem-Objekte aus der Datenbank
    todo_items = ToDoItem.objects.all()
    todo_items = ToDoItem.objects.filter(completed=False)

    # Übergebe die ToDoItem-Objekte an das Template
    return render(request, 'todo_list.html', {'todo_items': todo_items})



def todo_add(request):
    if request.method == 'POST':
        # If the form has been submitted, process the data
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # Redirect to the ToDo list after adding an item
    else:
        # If it's a GET request, create an empty form
        form = ToDoItemForm()

    return render(request, 'todo_add.html', {'form': form})


def update_completion_status(request):
    print('entering update_completion_status function')
    if request.method == 'POST':
        completed_item_ids = request.POST.getlist('completed_items')
        print('completed items: ' , completed_item_ids)
        ToDoItem.objects.filter(id__in=completed_item_ids).update(completed=True)

    return redirect('todo_list')