import time
from tqdm import tqdm

filename = "wu-tang-no-tags.txt"
profanity_file = "profanity_list.txt"


with open(profanity_file, "r") as file:
    content = file.read()
    content = content.rstrip()
    profanity = content.split(',')

print(len(profanity))
profanity.sort()
profanity.reverse()

content = ""
with open(filename, "r") as file:
    while True:
        x = file.readline()
        if not x:
            break

        x = x.lower()

        for word in profanity:
            start = x.find(word)
            if start == -1:
                pass
            else:
                end = len(word)

                x = x[:1 + start] + "PROFANITY" + x[start + end:]

        content += x

with open("wu-tang-no-tags-no-profanity.txt", "w") as file:
    file.write(content)
