def BetrothedNumbers(n) :
    for num1 in range (1,n) :
         sum1 = 1
         i = 2
         while i * i <= num1 :
              if (num1 % i == 0) :
                   sum1 = sum1 + i
                i =i + 1
