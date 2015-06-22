from search import base
from search import settings


def ask(query):
    response = settings.CLIENT.search(index=settings.ELASTIC_INDEX, doc_type='blame', body=base.build_query(query))
    hits = response['hits']['hits']
    user_aggs = response['aggregations']['per_user']['buckets']
    file_aggs = response['aggregations']['per_file']['buckets']
    results = {'hits': hits, 'user_aggs': user_aggs, 'file_aggs': file_aggs}
    return results
