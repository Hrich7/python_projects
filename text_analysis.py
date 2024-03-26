user_text = input("Please enter a text: ").lower()

print("Please Enter 3 random letters")
letter_one = input("First letter: ")[0].lower()
letter_two = input("Second letter: ")[0].lower()
letter_three = input("Third letter: ")[0].lower()

user_text_list = user_text.split()

print(f"'{letter_one}' appears {user_text.count(letter_one)} times in the text")
print(f"'{letter_two}' appears {user_text.count(letter_two)} times in the text")
print(f"'{letter_three}' appears {user_text.count(letter_three)} times in the text")

print("\n")
print(f"There are {len(user_text_list)} words in the text:\n{user_text_list}")

print(f"The first letter of the text is: '{user_text[0]}'\nThe last letter of the text is '{user_text[-1]}'\n")

inverted_text = " ".join(user_text_list[::-1])
print(f"If the words were in inverted order the text would be : \n{inverted_text}\n")


dic = {True : "was", False : "was not"}
is_python = "python" in user_text
print(f" The word python {dic[is_python]} found in your text")