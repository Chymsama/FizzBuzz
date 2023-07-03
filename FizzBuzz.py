#!/usr/bin/env python
# coding: utf-8

# In[1]:


start = int(input("Nhập số bắt đầu: "))
end = int(input("Nhập số kết thúc: "))

if end < start:
    print("Số kết thúc cần lớn hơn số bắt đầu!")
else:
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

