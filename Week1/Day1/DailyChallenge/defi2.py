user_word = input("Entrez un mot : ")
new_word = ""
for i in range(len(user_word)):
    if i == 0 or user_word[i] != user_word[i-1]:
        new_word += user_word[i]
print(f"user's word : {user_word} ➞ {new_word}")

