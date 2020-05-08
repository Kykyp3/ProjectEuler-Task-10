# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import time
start_time = time.time()

def find_primes_below(x):
    prime_numbers = [2,3]
    for i in range(5,x,2):
        for b in range(3,int(i**0.5)+2,2):
            if i % b == 0:
                break
            elif b+2>int(i**0.5):
                prime_numbers.append(i)
                break
    return prime_numbers

def sum_primes(n):
    prime_list = find_primes_below(n)
    sum_primes = 0
    for i in range(0,len(prime_list),1):
        sum_primes += prime_list[i]
    return sum_primes

if __name__=="__main__":
    print(sum_primes(2000000))

end_time = time.time()
print(end_time - start_time)