"""
* ask
"""
from supportbot.bots import FuzzyMatchingSupportbot


if __name__ == "__main__":
    import sys

    usage = f"Usage: python {sys.argv[0]} ask question"

    # bot = FuzzyMatchingSupportbot("../assets/questions_answers.txt")
    bot = FuzzyMatchingSupportbot("../assets/questions_answers_zh.txt")

    action = sys.argv[1:2]
    if action == ["ask"]:
        questions = sys.argv[2:3]
        if questions:
            result = bot.reply(questions[0])
            print(result)
        else:
            print(usage)
    else:
        print(usage)
