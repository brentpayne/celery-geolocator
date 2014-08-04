from django.shortcuts import render
from demoapp.tasks import xsum


def sum_task(request, a, b):
    promise = xsum.delay([a, b])
    result = promise.get()
    return render(
        request
        , 'demoapp/sum.html'
        , {
            'a': a
            , 'b': b
            , 'result': result
        }
    )

