from functools import lru_cache

from fuzzywuzzy import fuzz

from supportbot.common import read_questions_answers


class FuzzyMatchingSupportbot:
    def __init__(self, questions_answers_filepath):
        self.questions_answers = dict(
            read_questions_answers(questions_answers_filepath))

    @lru_cache()
    def reply(self, question):
        questions_partial_ratios = {}
        for _question, answer in self.questions_answers.items():
            # Minimum unit is character but not word.
            partial_ratio = fuzz.partial_ratio(question, _question)
            if partial_ratio > 0:  # find any match
                questions_partial_ratios[_question] = partial_ratio
        if questions_partial_ratios:
            matched_questions = sorted(
                questions_partial_ratios,
                key=lambda x: questions_partial_ratios[x],
                reverse=True)
            best_matched_question = matched_questions[0]
            return {
                "question": best_matched_question,
                "answer": self.questions_answers[best_matched_question],
            }
        else:
            return None
