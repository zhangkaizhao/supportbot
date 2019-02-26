import json

from supportbot.common import read_questions_answers

from helpers import get_fixture_filepath


def _test_read_questions_answers(filename, json_filename):
    filepath = get_fixture_filepath(filename)
    json_filepath = get_fixture_filepath(json_filename)

    with open(json_filepath) as f:
        expected = json.load(f)

    got = read_questions_answers(filepath)

    for _expected, _got in zip(expected, got):
        assert(tuple(_expected) == _got)


def test_read_questions_answers():
    filename = "questions_answers.txt"
    json_filename = "questions_answers.json"
    _test_read_questions_answers(filename, json_filename)


def test_read_questions_answers_zh():
    filename = "questions_answers_zh.txt"
    json_filename = "questions_answers_zh.json"
    _test_read_questions_answers(filename, json_filename)
