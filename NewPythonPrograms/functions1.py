import re
def vowel(s):
        Flag=False
        for i in s:
            if re.search("[aeiouAEIOU]",i):
                Flag=True
        if Flag:
            print("This is a vowel",s)
        else:
            print("This is a consonent",s)

vowel("sky")