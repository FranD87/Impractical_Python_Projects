
palindromes.py
Pseudocode:

Load digital dictionary file as a list of words.
Create an empty list to hole palindromes
Loop through each word in the word list:
    If word sliced forward is the same as word sliced backward:
        Append word to palindrome list
print palindrome list

palingrams.py
Pseudocode:

Load dictionary file as a list of words.
Star an empty list to hold palingrams
For word in word list:
    Get lenght of word
    If lenght > 1:
        Loop through the letters in the word:
            If reversed worf fragment at front of word is in word list and letters
            after form a palindromic sequence:
                Append word and reversed word to palingram list
            If reversed word fragment at end of word is in word list and letters
            before form a palindomic sequence:
                Append reversed word and word to palingram list
Sort paligram list alphabetically
Prin word-pair palingrams from palingram list
