from django.shortcuts import render

from maneu_class import service


def class_list(request):
    user_id = request.session.get('id')
    return render(request, 'maneu_class/class_list.html', {'classList': service.class_list(user_id=user_id)})


def class_insert(request):
    if request.method == 'POST':
        user_id = request.session.get('id')

    return render(request, 'maneu_class/class_insert.html')
