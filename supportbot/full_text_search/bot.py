import os
import os.path

import jieba
from whoosh.index import create_in, open_dir

from supportbot.common import read_questions_answers
from supportbot.full_text_search.index import schema
from supportbot.full_text_search.search import search


class FullTextSearchSupportbot:
    def __init__(self, index_dir):
        self.index_dir = index_dir

    @property
    def index(self):
        if not hasattr(self, "_index"):
            self._index = open_dir(self.index_dir)
        return self._index

    def create_index(self, questions_answers_filepath, words_filepath=None):
        """Create index from questions and their answers"""
        questions_answers = read_questions_answers(questions_answers_filepath)

        # User custom dictionary with new words can ensure a higher accuracy.
        if words_filepath is not None:
            jieba.load_userdict(words_filepath)

        if not os.path.exists(self.index_dir):
            os.makedirs(self.index_dir)

        ix = create_in(self.index_dir, schema)
        writer = ix.writer()

        for question, answer in questions_answers:
            writer.add_document(question=question, answer=answer)

        writer.commit()

        self._index = ix

    def reply(self, question):
        """Find a best matched question and its answer to asked question"""
        return search(self.index, question)
