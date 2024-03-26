def return_distincts(a, b, c):
    a_sum = a + b + c
    a_list = [a, b, c]
    if a_sum > 15:
        return max(a_list)
    elif a_sum < 10:
        return min(a_list)
    else:
        a_list.sort
        return a_list[1]

def consecutive_zeros(*args):
    counter = 0
    for _ in args:
        if counter + 1 == len(args):
            return False
        elif args[counter] == 0 and args[counter + 1] == 0 :
            return True
        else:
            counter += 1
    return False



def is_prime(number):
    prime = False
    if number <= 1:
        return False
    elif number <= 3 :
        return True
    else:
        for i in range(2, (number//2) + 1):
            if number % i == 0:
                return False
            else:
                return True

def count_primes(number):
    
    prime_numbers = [2]
    iteration = 3

    if number < 2 :
        return 0
    
    while iteration <= number:
        for n in range(3, iteration, 2):
            if iteration % n == 0:
                iteration += 2
                break
        else:
            prime_numbers.append(iteration)
            iteration += 2

    print(prime_numbers)
    return len(prime_numbers)