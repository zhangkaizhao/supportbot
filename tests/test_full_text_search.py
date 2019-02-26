from tempfile import TemporaryDirectory

from supportbot.bots import FullTextSearchSupportbot

from helpers import get_fixture_filepath


def _make_bot(index_dir, filename):
    filepath = get_fixture_filepath(filename)
    bot = FullTextSearchSupportbot(index_dir)
    bot.create_index(filepath)
    return bot


def test_full_text_search_reply():
    filename = "questions_answers.txt"
    question = "OK?"

    with TemporaryDirectory() as index_dir:
        bot = _make_bot(index_dir, filename)
        result = bot.reply(question)

    assert(question in result["question"])
    assert(result.get("answer") is not None)


def test_full_text_search_reply_none():
    filename = "questions_answers.txt"
    question = "找不到"

    with TemporaryDirectory() as index_dir:
        bot = _make_bot(index_dir, filename)
        result = bot.reply(question)

    assert(result is None)


def test_full_text_search_reply_zh():
    filename = "questions_answers_zh.txt"
    question = "你好"

    with TemporaryDirectory() as index_dir:
        bot = _make_bot(index_dir, filename)
        result = bot.reply(question)

    assert(question in result["question"])
    assert(result.get("answer") is not None)


def test_full_text_search_reply_zh_none():
    filename = "questions_answers_zh.txt"
    question = "讨厌啦"

    with TemporaryDirectory() as index_dir:
        bot = _make_bot(index_dir, filename)
        result = bot.reply(question)

    assert(result is None)


def test_full_text_search_words_reply():
    filename = "questions_answers_words.txt"
    question = "cannot find symbol"

    with TemporaryDirectory() as index_dir:
        bot = _make_bot(index_dir, filename)
        result = bot.reply(question)

    assert(question.upper() in result["question"].upper())
    assert(result.get("answer") is not None)


def test_full_text_search_words_reply_none():
    filename = "questions_answers_words.txt"
    question = "cannot find mars"

    with TemporaryDirectory() as index_dir:
        bot = _make_bot(index_dir, filename)
        result = bot.reply(question)

    assert(result is None)
