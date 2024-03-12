def second_largest(number):
    if len(number)<2:
        return none
    largest=float('-inf')
    second_largest=float('-inf')
     for num in number:
        if num>largest=largest
        largest=num
    elif num>second_largestand num!=largest:
        second_largest=num
    if second_largest==float('-inf'):
        return none
    else:
        return second_largest
number=[10,5,7,20,15]
second_largest=find_second_largest(number)
if  second_largest is  none :
    print("there is no second largest number:{second_largest}")
else:
    print(f"the second largest number is :{second_largest}")