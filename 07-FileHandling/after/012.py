#liczenie samogłosek

import re

pattern = "[eyuioaEYUIOA]"
message = "To be, or not to be, that is the question"

vovels = re.findall(pattern, message)

print(f"Number of vovels: {len(vovels)}")