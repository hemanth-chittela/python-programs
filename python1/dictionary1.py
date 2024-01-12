students=[{
            "name":"cat",
            "age":10,
            "school":"MNR"
            },
                {
                    "name":"ashok",
                    "age":11,
                    "school":"MNR1"
                }
            ]

for i in (students):
    print(i["name"],i["school"])

cat=[(cat["name"], cat["school"], cat["age"])for cat in students]
print(cat)