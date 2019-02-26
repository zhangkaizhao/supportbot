from jieba.analyse.analyzer import ChineseAnalyzer
from whoosh.fields import Schema
from whoosh.fields import TEXT


analyzer = ChineseAnalyzer()

schema = Schema(
    question=TEXT(stored=True, analyzer=analyzer),
    answer=TEXT(stored=True),
)
