'''
calculate how many zero(0)s in the end of n!.
'''


def zero_cnt_of_factorial(num):
    count = 0
    
    while num/5:
        count += num/5
        num /= 5
        
    return count

if __name__ == '__main__':
    n = int(raw_input('Enter a number: '))
    print "{0} has {1} zeros in the end.".format(n, zero_cnt_of_factorial(n))
