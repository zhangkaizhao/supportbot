from whoosh.qparser import QueryParser


def search(ix, text):
    with ix.searcher() as searcher:
        parser = QueryParser("question", schema=ix.schema)
        query = parser.parse(text)
        results = searcher.search(query, limit=1)
        result = dict(results[0]) if results else None
    return result
