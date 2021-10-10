# Submition for Source Code Poetry 2021
# https://www.sourcecodepoetry.com
# Author: Williangl
# Python 3.9+
"""
Gray day

Days that you feel gray
Like sky in the rain
That you feel bad
When a hug is not so bad
And a support phrase could help
"""
from datetime import datetime


class GrayDays():
    def that_you_feel(self, emotion):
        if emotion == "gray":
            return "Like sky in the rain"
        if emotion == "bad":
            when = datetime.now().strftime("%Y/%m/%d")
            return f"{when=} a hug is not so bad"


days = GrayDays()

print(f"{days.that_you_feel('gray')=}")
print(f"{days.that_you_feel('bad')=}")
print("And a suport phrase could help!! \N{people hugging}")
