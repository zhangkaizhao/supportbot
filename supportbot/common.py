import itertools


def read_questions_answers(filepath):
    """Read questions and their answers

    Format in input file:

      question 1
      answer 1

      question 2
      answer 2

      question 3
      answer 3
    """
    with open(filepath, "r") as f:
        lines = f.readlines()

    lines_iter = iter(lines)
    for three_lines in itertools.zip_longest(lines_iter, lines_iter, lines_iter):
        question, answer, _ = three_lines
        question = question.strip()
        answer = answer.strip()
        if question and answer:
            yield question, answer
