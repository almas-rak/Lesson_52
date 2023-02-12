from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_view(request: WSGIRequest):
    first = int(request.GET.get('first', 0))
    second = int(request.GET.get('second', 0))
    method = (request.GET.get('method', ''))
    print(first)
    print(second)
    print(method)
    match method:
        case '-':
            result = first - second
        case '+':
            result = first + second
        case '*':
            result = first * second
        case _:
            result = 0
    # print(f"id {request.GET.get('id')}")
    # print(f'name {request.GET.get("name")}')
    print(f"METHOD:  {request.method}")
    # print(f"Get id - {request.GET.get('id')} - {type(request.GET.get('id'))}")
    print(request)
    print(request.GET)
    return render(request, 'index.html', context={
        'result': result,
        'first': first,
        'second': second,
        'method': method
    })

# context={
#         'id': request.GET.get('id', 'no id'),
#         'name': request.GET.get("name", 'no name')
#
#     }
