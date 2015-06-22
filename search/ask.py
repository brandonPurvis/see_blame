from search import base
from search import settings


def ask(query):
    response = settings.CLIENT.search(index=settings.ELASTIC_INDEX, doc_type='blame', body=base.build_query(query))
    hits = response['hits']['hits']
    aggs = response['aggregations']['per_user']['buckets']
    for agg in aggs:
        score = agg['doc_count']
    results = {'hits': hits, 'aggs': aggs}
    return results
