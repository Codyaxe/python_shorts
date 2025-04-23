with open("test.txt", "a+") as text:

    text.write("101112\n")
    text.seek(0)
    print(text.read())
    text.seek(0)
    lines = text.readlines()

print("Test: ")
line_string = ''
for line in lines:
        line_string += line.strip()

print(line_string)

with open("newtext.txt", "w") as w:
      w.write("Hello Everyone!")