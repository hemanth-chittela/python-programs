def replaceWords(self, dictionary: list [str], sentence: str) -> str:
        sentence=list(sentence.split(" "))
        for i in range(len(dictionary)):  
            for j in range(len(sentence)):
                if dictionary[i][0]==sentence[j][0]:
                    if len(sentence[j])==2:
                        print(sentence)
                    else:
                        sentence[j]==dictionary[i]
        sentence=" ".join(sentence)
        return sentence

t=replaceWords(["cat","bat","rat"],"the cattle was rattled by the battery")
print(t)
