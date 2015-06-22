from elasticsearch_dsl import Q, F, Search


def build_query(search_text, from_=0, size=10):
    query = {
        'from': from_,
        'size': size,
        'query': {
            'query_string': {
                'default_field': '_all',
                'query': search_text,
                'analyze_wildcard': True,
                'lenient': True,
            }
        },
        'aggs': {
            'per_user': {
                'terms': {'field': 'uname'}
            }
        }
    }
    return query


def query_match(field, value):
    return Q('match', **{field: value})


def query_string(field, value):
    return Q('query_string',
             fields=field.split(' '),
             query=value,
             analyze_wildcard=True,
             )


def filter_term(field, value):
    return F('term', **{field: value})


class Query:
    def __init__(self):
        self.queries = []
        self.filters = []
    
    def add_string_query(self, value, field=None):
        field = field or '_all'
        self.queries.append(query_string(field, value))
    
    def add_match_query(self, field, value):
        self.queries.append(query_match(field, value))

    def add_filter_term(self, field, value):
        self.queries.append(filter_term(field, value))

    @property
    def query(self):
        search_obj = Search()
        for f in self.filters:
            search_obj = search_obj.filter(f)

        for q in self.queries:
            search_obj = search_obj.query(q)

        return search_obj.to_dict()
