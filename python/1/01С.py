Требуется написать программу, которая считывает число и выводит Fizz, если число делится на 3, 
Buzz, если число делится на 5, 
и FizzBuzz, если оно делится и на 3, и на 5. 
Если число не делится ни на 3, ни на 5, вывести пустую строку (перевод строки).

N = int(input())
if (N%3==0):
    if(N%5 == 0):
        print("FizzBuzz")
    else:
        print("Fizz")
elif (N%5==0):
    print("Buzz")
else:
    print()
