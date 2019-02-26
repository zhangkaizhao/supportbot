from supportbot.bots import FuzzyMatchingSupportbot

from helpers import get_fixture_filepath


def _make_bot(filename):
    filepath = get_fixture_filepath(filename)
    return FuzzyMatchingSupportbot(filepath)


def test_fuzzy_matching_reply():
    filename = "questions_answers.txt"
    question = "OK?"

    bot = _make_bot(filename)
    result = bot.reply(question)

    assert(question in result["question"])
    assert(result.get("answer") is not None)


def test_fuzzy_matching_reply_none():
    filename = "questions_answers.txt"
    question = "找不到"

    bot = _make_bot(filename)
    result = bot.reply(question)

    assert(result is None)


def test_fuzzy_matching_reply_zh():
    filename = "questions_answers_zh.txt"
    question = "你好"

    bot = _make_bot(filename)
    result = bot.reply(question)

    assert(question in result["question"])
    assert(result.get("answer") is not None)


def test_fuzzy_matching_reply_zh_none():
    filename = "questions_answers_zh.txt"
    question = "讨厌啦"

    bot = _make_bot(filename)
    result = bot.reply(question)

    assert(result is None)
