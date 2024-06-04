from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline

from catalog.models import Products


def q_search(query):

    if query.isdigit():
        return Products.objects.filter(id=int(query))
    

    keywords = [word for word in query.split()]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(articul__icontains=token)
        q_objects |= Q(name__icontains=token)

    
    return Products.objects.filter(q_objects)
