string = "IceCreAm"
vowels = "aeiouAEIOU"
s_list = list(string)

# Collect the vowels in order
vowel_chars = [c for c in s_list if c in vowels]

print(vowel_chars)