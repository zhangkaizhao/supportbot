"""
* create_index
* ask
"""
from supportbot.bots import FullTextSearchSupportbot


if __name__ == "__main__":
    import sys

    usage = (f"Usage: python {sys.argv[0]} create_index|ask question"
             "\n(Note: create index before asking question)")

    bot = FullTextSearchSupportbot("index_dir")

    action = sys.argv[1:2]
    if action == ["create_index"]:
        # bot.create_index("../assets/questions_answers.txt")
        bot.create_index("../assets/questions_answers_zh.txt")
    elif action == ["ask"]:
        questions = sys.argv[2:3]
        if questions:
            result = bot.reply(questions[0])
            print(result)
        else:
            print(usage)
    else:
        print(usage)
