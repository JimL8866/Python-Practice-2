# import random
# card_color_list = ["heart", "spade", " diamond", "club"]
# card_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # A
# all_card_list = [[color, num] for color in card_color_list for num in card_nums]   #list comprehension
# random.shuffle(all_card_list)
# print(all_card_list)

# user_list = []
# while True:
#     user = input("Please put in username(Q for quit)：")
#     if user == "Q":
#         break
#     pwd = input("Please put in password：")
#     data = [user,pwd]         #store data in a list
#     user_list.append(data)

# print(user_list)

# num ="10"
# print(num.isdecimal())

# with open("1.png", "rb") as file:
#     content = file.read()
#     print(content)

# with open("2.png", "wb") as file2:
#     file2.write(content)

# import os

# path = os.path.exists(r"C:\Users\Owner\OneDrive\Documents\GitHub\Python Module\2.png")
# print(path)

# my_list = [1, 3, 4, 5, 1, 4, 7]
# my_list2 = set(my_list)

# print(list(my_list2))


# str="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
# dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
# proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
# """

# with open("text.txt", "w") as file:
#     file.write(str)

# import requests

# res = requests.get(url="https://loremipsum.io/")

# headers={
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
#     }


# print(res.content)

# total = 0
# #your code goes here
# price = 100
# sum_price= 0
# while total < 5:
#     total += 1
#     age = int(input("ages"))
#     if age < 3:
#         continue
#     sum_price = age * price

# print(sum_price)

# from re import M


# m =[
#     [1,2,3],
#     [4,5,6],
# ]
# print(m)

# import smtplib
# email = "zeric206@gmail.com"  # sender email
# pwd = "1234567PO"  # sender pwd
# addrs_list = ["hahahwang123@gmail.com",
#               "liucy035@gmail.com", "jimliujob@gmail.com"]


# with smtplib.SMTP("smtp.gmail.com") as connection:  # create obj
#     connection.starttls()
#     connection.login(user=email, password=pwd)
#     for item in addrs_list:

#         connection.sendmail(
#             from_addr=email,
#             to_addrs=item,
#             msg="Subject:How are you?\n\nThis is the body of my email"
#         )

# import datetime as dt
# now = dt.datetime.now()
# print(type(now))
# print(now.year)


# import requests
# from xml.etree import ElementTree as ET


# def xml_to_list(city):
#     data_list = []
#     url = "http://ws.webxml.com.cn//WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName={}".format(city)
#     res = requests.get(url=url)
#     print(res)
#     root = ET.XML(res.text)
#     for node in root:
#         data_list.append(node.text)
#     return data_list


# result = xml_to_list("北京")
# print(result)

# def num(x):
#     num = x +8


# res = num(8)
# print(res)


# list1 = [1, 3]
# print(id(list1))

# list1.append(4)
# print(list1)
# print(id(list1))   # list is mutable

# str ="Hello#"
# print(id(str))
# str.replace("#","")
# print(id(str))     # string is unmutable create new string
