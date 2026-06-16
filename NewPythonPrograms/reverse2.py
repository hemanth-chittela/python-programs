string="the sky is blue"
final_string=""
s=string.strip()
s=s.split()
print(s)
for i in range(len(s)-1,-1,-1):
    final_string=final_string+" "+s[i]
final=final_string.strip()
print(final)
