def is_prime(func):
    def truth(*args, **kwargs):
        result = func(*args, **kwargs)
        sum_1 = sum(args)
        a = 0
        for i in range(2, sum_1 // 2 +1):
            if sum_1 % i  == 0:
                a = a +1
        if a <= 0:
            print('Простое')
        else:
            print("Составное")
        return result
    return truth

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3 ,6)
print(result)
