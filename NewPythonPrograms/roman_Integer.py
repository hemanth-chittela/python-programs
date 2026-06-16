roman_values={ 1000:"M",
              900:"CM",
              500:"D",
              400:"CD",
              100:"C",
              90:"XC",
              50:"L",
              40:"XL",
              10:"X",
              9:"IX",
              5:"V",
              4:"IV",
              1:"I"
              }
in_roman=""
number=int(input("Enter the number: "))
for value in roman_values:
    while number>=value:
        in_roman=in_roman+roman_values[value]
        number=number-value
print(in_roman)