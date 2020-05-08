# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import time
start_time = time.time()

def sum_primes_below(x):
    prime_numbers = 5 # 2 and 3
    for i in range(5,x,2):
        for b in range(3,int(i**0.5)+2,2):
            if i % b == 0:
                break
            elif b+2>int(i**0.5):
                prime_numbers +=i
                break
    return prime_numbers

if __name__=="__main__":
    print(sum_primes_below(2000000))

end_time = time.time()
print(end_time - start_time)