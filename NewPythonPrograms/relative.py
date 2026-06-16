score=[1,2,3,4,5,6,7,8,9,10]
ranks=[]
count=0
for i in range(len(score)):
    for j in range(len(score)):
        if len(score)<=5 and score[i]>score[j]:
            count=count+1
        elif len(score)>=5 and score[i]>=score[j]:
             count=count+1
    if len(score)==1:
         ranks.append("Gold Medal")
         count=0
    elif len(score)==2 and count==1:
         ranks.append("gold Medal")
         count=0
    elif len(score)==2 and count==0:
         ranks.append("Silver Medal")
         count=0
    elif len(score)==3 and count==2:
         ranks.append("gold Medal")
         count=0
    elif len(score)==3 and count==1:
         ranks.append("Silver Medal")
         count=0
    elif len(score)==3 and count==0:
         ranks.append("Bronze Medal")
         count=0
    elif len(score)==2 and count==1:
         ranks.append("Bronze")
         count=0
    elif len(score)==4 and count==3:
         ranks.append("gold Medal")
         count=0
    elif len(score)==4 and count==2:
         ranks.append("Silver Medal")
         count=0
    elif len(score)==4 and count==1:
         ranks.append("Bronze Medal")
         count=0
    elif len(score)==4 and count==0:
         ranks.append("4")
         count=0
    elif len(score)==5 and count==5:
         ranks.append("Gold Medal")
         count=0
    elif len(score)==5 and count==4:
         ranks.append("Silver Medal")
         count=0
    elif len(score)==5 and count==3:
         ranks.append("Bronze Medal")
         count=0
    elif len(score)==5 and count==2:
         ranks.append("4")
         count=0
    elif len(score)==5 and count==1:
         ranks.append("5")
         count=0
    elif len(score)>=5 and count<len(score)-4:
         ranks.append(str(len(score)+1-count))
         count=0
    elif len(score)>=5 and len(score)-count==4:
         ranks.append("5")
         count=0
    elif len(score)>=5 and len(score)-count==3:
         ranks.append("4")
         count=0
    elif len(score)>=5 and len(score)-count==2:
         ranks.append("Bronze Medal")
         count=0
    elif len(score)>=5 and len(score)-count==1:
         ranks.append("Silver Medal")
         count=0
    elif len(score)>=5 and len(score)-count==0:
         ranks.append("Gold Medal")
         count=0

print(ranks)