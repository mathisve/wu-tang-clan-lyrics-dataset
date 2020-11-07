import os
import re

remove_tags = True

content = ""
for file in os.listdir("scrapes"):
    with open("scrapes/{}".format(file), "r") as file:
        prev = True
        while True:
            x = file.readline()
            if not x:
                break

            if "\n" == x:
                if prev == True:
                    prev = True
                    continue
                prev = True

            if remove_tags:
                if "[" in x and "]" in x:
                        continue


            content += x
            prev = False


with open("wu-tang.txt", "w") as file:
    file.write(content.rstrip())
