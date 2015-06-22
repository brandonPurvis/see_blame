from django.shortcuts import render
from .forms import QueryForm
from search.ask import ask


def search(request):
    form = QueryForm()
    results = []
    aggs = []
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            results = ask(form.cleaned_data['query'])
            aggs = results['aggs']
            results = results['hits']

            results = list(map(lambda r: r['_source'], results))
    context = {'results': results,
               'aggs': aggs,
               'form': form,
               }
    return render(request, 'main.html', context)
