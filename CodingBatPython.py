## Python exercises from https://codingbat.com/python

## Warmup-1 - Sleep_in
## The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
##sleep_in(False, False) → True
##sleep_in(True, False) → False
##sleep_in(False, True) → True

#def sleep_in(weekday, vacation):
#    if weekday ==  False or vacation == True:
#        return True
#    else:
#        return False

#print(sleep_in(False, False))
#print(sleep_in(True, False))
#print(sleep_in(False, True))

## We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
##monkey_trouble(True, True) → True
##monkey_trouble(False, False) → True
##monkey_trouble(True, False) → False

#def monkey_trouble(a_smile, b_smile):
#    if a_smile == b_smile:
#        return True
#    else:
#        return False

#print(monkey_trouble(True, True))
#print(monkey_trouble(False, False))
#print(monkey_trouble(True, False))

## Given two int values, return their sum. Unless the two values are the same, then return double their sum.
## sum_double(1, 2) → 3
## sum_double(3, 2) → 5
## sum_double(2, 2) → 8

#def sum_double(a, b):
#    if a == b:
#        return (a + b) * 2
#    else:
#        return ( a + b )

#print(sum_double(1, 2))
#print(sum_double(3, 2))
#print(sum_double(2, 2))

## Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
## diff21(19) → 2
## diff21(10) → 11
## diff21(21) → 0

#def diff21(n):
#    if n > 21:
#        return 2 * (n-21)
#    else:
#        return abs(n-21)

#print(diff21(19))
#print(diff21(10))
#print(diff21(21))
 

## We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.       
##parrot_trouble(True, 6) → True
##parrot_trouble(True, 7) → False
##parrot_trouble(False, 6) → False

#def parrot_trouble(talking, hour):
#    if talking == True and (hour < 7 or hour > 20):
#        return True
#    else:
#        return False

#print(parrot_trouble(True, 6))
#print(parrot_trouble(True, 7))
#print(parrot_trouble(False, 6))

## Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
## makes10(9, 10) → True
## makes10(9, 9) → False
## makes10(1, 9) → True

#def makes10(a, b):
#    if ( a == 10) or (b == 10) or ((a + b) == 10):
#        return True
#    else:
#        return False

#print(makes10(9, 10))
#print(makes10(9, 9))
#print(makes10(1, 9))

## Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
## near_hundred(93) → True
## near_hundred(90) → True
## near_hundred(89) → False

#def near_hundred(n):
#    if abs(100 -n)<=10 or abs(200 -n)<=10:
#        return True
#    else:
#        return False

#print(near_hundred(93))
#print(near_hundred(90))
#print(near_hundred(89))

## Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
## pos_neg(1, -1, False) → True
## pos_neg(-1, 1, False) → True
## pos_neg(-4, -5, True) → True

#def pos_neg(a, b, negative):
#    if (negative == True and a < 0 and b < 0) or (negative == False and a * b < 0):
#        return True
#    else:
#        return False
#print(pos_neg(1, -1, False))
#print(pos_neg(-1, 1, False))
#print(pos_neg(-4, -5, True))

## Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.  
## not_string('candy') → 'not candy'
## not_string('x') → 'not x'
## not_string('not bad') → 'not bad'

#def not_string(str):
#    if (str[:3]) == "not":
#        return str
#    else:
#        return "not " + str
#print(not_string('candy'))
#print(not_string('x'))
#print(not_string('not bad'))


## Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
## missing_char('kitten', 1) → 'ktten'
## missing_char('kitten', 0) → 'itten'
## missing_char('kitten', 4) → 'kittn'

#def missing_char(str, n):
#    out_str = ""
#    i = 0
#    for my_char in str:
#        if n != i:
#            out_str = out_str + my_char
#        i+=1
#    return out_str
#print(missing_char('kitten', 1))
#print(missing_char('kitten', 0))
#print(missing_char('kitten', 4))

## Given a string, return a new string where the first and last chars have been exchanged.
## front_back('code') → 'eodc'
## front_back('a') → 'a'
## front_back('ab') → 'ba'

#def front_back(str):
#    i = len(str)-1
#    out_str = ""
#    while i >= 0:
#        out_str = out_str + str[i]
#        i = i - 1
#    return out_str  

#print(front_back('code'))
#print(front_back('hello'))
#print(front_back('Chocolate'))

## Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
## front3('Java') → 'JavJavJav'
## front3('Chocolate') → 'ChoChoCho'
## front3('abc') → 'abcabcabc'

#def front3(str):
#    mystr = str[:3]
#    return mystr * 3

#print(front3('Java'))
#print(front3('Chocolate'))
#print(front3('abc'))

## Warmaup-2

## Given a string and a non-negative int n, return a larger string that is n copies of the original string.
## string_times('Hi', 2) → 'HiHi'
## string_times('Hi', 3) → 'HiHiHi'
## string_times('Hi', 1) → 'Hi'

#def string_times(str, n):
#    return str * n
#print(string_times('Hi', 2))
#print(string_times('Hi', 3))
#print(string_times('Hi', 1))

## Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
## front_times('Chocolate', 2) → 'ChoCho'
## front_times('Chocolate', 3) → 'ChoChoCho'
## front_times('Abc', 3) → 'AbcAbcAbc'

#def front_times(str, n):
#    return str[:3] * n
# print(front_times('Chocolate', 2))
# print(front_times('Chocolate', 3))
# print(front_times('Abc', 3))


## Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
## string_bits('Hello') → 'Hlo'
## string_bits('Hi') → 'H'
## string_bits('Heeololeo') → 'Hello'

#def string_bits(str):
#    i = 0
#    out_str = ""
#    while i <= len (str) - 1:
#        if i % 2 == 0:
#            out_str += str[i]
#        i+=1
#    return out_str

#print(string_bits('Hello'))
#print(string_bits('Hi'))
#print(string_bits('Heeololeo'))


## Given a non-empty string like "Code" return a string like "CCoCodCode".
## string_splosion('Code') → 'CCoCodCode'
## string_splosion('abc') → 'aababc'
## string_splosion('ab') → 'aab'

#def string_splosion(str):
#    i=0
#    out_str=""
#    while i <= len (str):
#        out_str += str[:i]
#        i = i+1
#    return out_str

#print(string_splosion('Code'))
#print(string_splosion('abc'))
#print(string_splosion('ab'))


##   Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
## last2('hixxhi') → 1
## last2('xaxxaxaxx') → 1
## last2('axxxaaxx') → 2

## ???????????????????????


## Given an array of ints, return the number of 9's in the array.
## array_count9([1, 2, 9]) → 1
## array_count9([1, 9, 9]) → 2
## array_count9([1, 9, 9, 3, 9]) → 3

#def array_count9(nums):
#    i = 0
#    for int_c in nums:
#        if int_c == 9:
#            i += 1
#    return i
#print(array_count9([1, 2, 9]))
#print(array_count9([1, 9, 9]))
#print(array_count9([1, 9, 9, 3, 9]))



## Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
## array_front9([1, 2, 9, 3, 4]) → True
## array_front9([1, 2, 3, 4, 9]) → False
## array_front9([1, 2, 3, 4, 5]) → False

#def array_front9(nums):
#    i = False
#    for int_c in nums[:4]:
#        if int_c == 9:
#            i = True
#    return i
#print(array_front9([1, 2, 9, 3, 4]))
#print(array_front9([1, 2, 3, 4, 9]))
#print(array_front9([1, 2, 3, 4, 5]))


## Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
## array123([1, 1, 2, 3, 1]) → True
## array123([1, 1, 2, 4, 1]) → False
## array123([1, 1, 2, 1, 2, 3]) → True

#def array123(nums):
#    count = 0
#    while count <= len(nums) :
#        if nums[count:count+3] == [1,2,3]:
#            return True
#        count += 1
#    return False

#print(array123([1, 1, 2, 3, 1]))
#print(array123([1, 1, 2, 4, 1]))
#print(array123([1, 1, 2, 1, 2, 3]))


## Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
## string_match('xxcaazz', 'xxbaaz') → 3
## string_match('abc', 'abc') → 2
## string_match('abc', 'axc') → 0

#def string_match(a, b):
#    i = 0
#    count = 0
#    while i <= len(a)-2:
#        if a[i:i+2] == b[i:i+2]:
#            count += 1
#        i+=1
#    return count

#print(string_match('xxcaazz', 'xxbaaz'))
#print(string_match('abc', 'abc'))
#print(string_match('abc', 'axc'))


## Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
## hello_name('Bob') → 'Hello Bob!'
## hello_name('Alice') → 'Hello Alice!'
## hello_name('X') → 'Hello X!'

#def hello_name(name):
#    return("Hello " + name + "!")
#hello_name("Pino")


##Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
##make_abba('Hi', 'Bye') → 'HiByeByeHi'
##make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
##make_abba('What', 'Up') → 'WhatUpUpWhat'

#def make_abba(a, b):
#    return(a + b + b + a)
#print(make_abba("ciao","----"))


## The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
## make_tags('i', 'Yay') → '<i>Yay</i>'
## make_tags('i', 'Hello') → '<i>Hello</i>'
## make_tags('cite', 'Yay') → '<cite>Yay</cite>'

#def make_tags(tag, word):
#    return("<" + tag + ">" + word + "<" + tag + ">")
#print(make_tags('i', 'Yay'))
#print(make_tags('i', 'Hello'))
#print(make_tags('cite', 'Yay'))


## Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
## extra_end('Hello') → 'lololo'
## extra_end('ab') → 'ababab'
## extra_end('Hi') → 'HiHiHi'




















