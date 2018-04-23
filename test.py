# def quicksort (A, lo, hi):
#     if lo < hi:
#         p = partition(A, low, hi)
#
# def partition(A ,lo, hi):
#     pivot = A[hi]
#     i = lo -1
#     for j in range(lo,hi-1):
#         if A[j] < pivot:
#             i+= 1
#             temp = A[i]
#             A[i] = A[j]
#             A[j] = temp
#     temp = A[i+1]
#     A[i + 1] = hi
#     hi = temp
#     return i + 1
#
#     A = [1,3,6,10,100,10000,4,2,60,100]
#     # print(quicksort(A, 1, 10000))
#
# j = 97
# chars = []
# for i in range(0,26):
#     chars.append(chr(j))
#     j+=1
# print(chars)
#
# def factorial(input):
#     sum = input
#     for i in range(input, 0,-1):
#         sum *= i
#     return sum
# print(factorial(5))

def findIntersect(line0a, line0b, line1a, line1b):
    m0= (line0b[1] - line0a[1]) / (line0a[0] - line0b[1])
    b0 = line0a[1] - m0 * line0a[0]
    m1 = (line1b[1] - line1a[1]) / (line1a[0] - line1b[1])
    b1 = line1a[1] - m1 * line1a[0]
    intercept
    intercept[0] = (b1 - b0) / (m0 - m1);
    intercept[1] = m0 * intercept[0] + b0;
    return intercept

numbers = []
for i in range(0,99):
    numbers.append(i)

print Sieve(numbers)

def Sieve(numbers):
    skip[100] = false
    for i in numbers:
        if not skip[i]:
            for j in numbers:
                if j%i ==0:
                    skip[j] == true
    returns
    for i in range(0,100):
        if skip[i] == false:
            returns.append(number[i])
