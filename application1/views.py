from django.http import HttpResponse, HttpRequest, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
import os
from random import choice

articles = {
    'sports': "Sports Page",
    'finances': "Finance Page",
    'culture': "Culture Page",
}


def news_view(request: HttpRequest, topic: str):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])

    except :
        raise Http404('GENERIC ERROR')


def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]
    return HttpResponseRedirect(topic)


def home_view(request):
    pokes = r'application1\static\images'
    context = {}
    pokemons = [file for _, _, file in os.walk(pokes)][0]
    rand_poke = choice(pokemons)
    context['poke_to_view'] = f'{rand_poke}'
    context['poke_name'] = rand_poke.removesuffix('.png').split('_')[1]
    return render(request, 'pokemon.html', context=context)


