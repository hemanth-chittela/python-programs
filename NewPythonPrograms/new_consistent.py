class Solution:
    def largestGoodInteger(self, num: str) -> str:
        new_list=""
        number_list=[]
        new_dicto={}
        maximum_numbers=[]
        count=0
        finally_number_list=[]
        final_string=""
        for i in range(len(num)-1):
            if num[i]==num[i+1]:
                if count<=0:
                    new_list=new_list+num[i]+num[i+1]
                    count=count+1
                else:
                    new_list=new_list+num[i+1]
                    count=0
        other_list=list(new_list)
        
        if len(other_list)<3:
            return final_string
        else:
            for k in other_list:
                if k in new_dicto:
                    new_dicto[k]=new_dicto[k]+1
                else:
                    new_dicto[k]=1
            for key1,value1 in new_dicto.items():
                if value1>=3:
                    maximum_numbers.append((int(key1),value1))
            new_max=max(maximum_numbers)
            final_maximum=new_max[0]

            for x in range(3):
                final_string=final_string+str(final_maximum)
            return final_maxim

S=Solution()
S.largestGoodInteger("6777133339")

        