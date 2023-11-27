#liczenie słów

import re

pattern = " "
message = "To be, or not to be, that is the question"

words = re.findall(pattern, message)

print(f"Number of words: {len(words)+1}")