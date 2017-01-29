#!/usr/bin/env python
#-*-coding:utf-8-*-
#if..else
user="aaa"
passwd="123"

username=input("input a username:")
password=input("input a password:")

if user == username and passwd == password:
    print("wellcome login")
else:
    print("invalid username or password")

# if user == username:
#     print("username is correct...")
#     if passwd == password:
#         print("wellcome login")
#     else:
#         print("password is invalid")
# else:
#     print("username is invalid")

