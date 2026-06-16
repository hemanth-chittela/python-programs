new_list={}
ransom_note_list={}
ransom_note="aa"
magazine="aab"
Flag=True
for character in magazine:
    if character in new_list:
        new_list[character]=new_list[character]+1
    else:
        new_list[character]=1
print(new_list)
for character1 in ransom_note:
    if character1 in ransom_note_list:
        ransom_note_list[character1]=ransom_note_list[character1]+1
    else:
        ransom_note_list[character1]=1
print(ransom_note_list)

for ch in ransom_note_list:
    if ch not in new_list or new_list[ch]<ransom_note_list[ch]:
        Flag=False
        break
if Flag:
    print("True")
else:
    print(False)