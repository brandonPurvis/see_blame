from django.shortcuts import render
from .forms import QueryForm
from search.ask import ask


def search(request):
    form = QueryForm()
    results = []
    user_aggs = []
    file_aggs = []
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            results = ask(form.cleaned_data['query'])
            user_aggs = results['user_aggs']
            file_aggs = results['file_aggs']
            results = results['hits']
            print(file_aggs)
            results = list(map(lambda r: r['_source'], results))
    context = {'results': results,
               'user_aggs': user_aggs,
               'file_aggs': file_aggs,
               'form': form,
               }
    return render(request, 'main.html', context)
