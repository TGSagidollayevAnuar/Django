from django.shortcuts import render
from datetime import date


table = {
    'done': {
        'todos': [
            {
                'task': 'task1',
                'created': date.today().strftime("%d%m%y"),
                'due_on': date.today().strftime("%d%m%y"),
                'owner': 'admin',
                'mark': 'Done'
            },
            {
                'task': 'task2',
                'created': date.today().strftime("%d%m%y"),
                'due_on': date.today().strftime("%d%m%y"),
                'owner': 'admin',
                'mark': 'Done'

            },
            {
                'task': 'task3',
                'created': date.today().strftime("%d%m%y"),
                'due_on': date.today().strftime("%d%m%y"),
                'owner': 'admin',
                'mark': 'Done'
            },
        ]
    },
    'not_done': {
        'todos': [
            {
                'task': 'task4',
                'created': date.today().strftime("%d%m%y"),
                'due_on': date.today().strftime("%d%m%y"),
                'owner': 'admin',
                'mark': 'Not Done'
            },
        ]
    }
}


#views
def todo_list(request):
    return render(request, 'todo_list.html', table=table['not_done'])


def completed_todo_list(request):
    return render(request, 'completed_todo_list.html', table=table['done'])