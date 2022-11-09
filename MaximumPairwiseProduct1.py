#Goal: Maximum Pairwise Product
#Requirement: Working in less than one second even on huge datasets
#!/usr/bin/env python
# coding: utf-8


def max_pairwise_product(numbers):
    n = len(numbers)
    numbers.sort()
    return numbers[n-2] * numbers[n-1]
if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))




