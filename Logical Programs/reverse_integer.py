def reverse_integer(num):
    reversed=0
    while num!=0:
        digit=num%10
        reversed=reversed*10+digit
        num//=10
    return reversed

print(reverse_integer(1234))