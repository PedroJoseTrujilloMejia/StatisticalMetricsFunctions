import math
import numpy
import statistics

#empty list
alist = []

# number of numbers allowed for input
number = int(input("how many numbers do you want to add to the list? "))

for x in range(0,number):
    number = int(input())
    alist.append(number)
    
def sum_of_two_numbers(n1,n2):
    sum = n1+n2
    return sum

def sum_of_a_list(alist):
    sumoflist = sum(alist)
    return sumoflist

def average_of_a_list(alist):
    averagenumber = float(sum(alist))/float(len(alist))
    return averagenumber

def standard_deviation_of_a_list(alist):
    sdev = numpy.std(alist)
    return sdev

def median(alist):
    return statistics.median(alist)
    
print("Sdev of a list: " , standard_deviation_of_a_list(alist))
print("Sum of a list: ", sum_of_a_list(alist))
print("Average of a list: " , average_of_a_list(alist))
print("Median: ", median(alist))
