import load_dictionary

word_list = load_dictionary.load('load_dict.txt')

anagram_list = []

# input a SINGLE word or SINGLE name below to find it's anagram(s):

name = 'Foster'
print(f"name = {name}")

name = name.lower()
print(f"Using name = {name}")

# Sort name and find anagrams
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

#print out list of anagrams

print()
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name!")
else:
    print("Anagrams=", *anagram_list, sep='\n')


