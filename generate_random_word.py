def line_has_digit(line):
    return any(char.isdigit() for char in line)

# with open('wordlist.txt') as f:
#     for line in f:
#         if not line_has_digit(line):
#             print(line.strip())

wordlist = []
with open('wordlist2.txt') as file:
    for line in file:
        wordlist.append(line.strip())

print(wordlist)