#ЗАДАНИЕ №2
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x or (not(y))) and (not(y == z)) and (not(w))) == True:
#                     print(x, y, z, w)

#ЗАДАНИЕ №5
# def R(n):
#     n2 = bin(n)[2:]
#     if n % 3 == 0:
#         n2 += n2[-3:]
#     else:
#         n2 += bin((n % 3)*3)[2:]
#     return int(n2, 2)
# for n in range(1, 100):
#     if R(n) >= 76:
#         print(n)
#         break

#ЗАДАНИЕ №5 - ТРОИЧНАЯ
# def troic(n):
#     n3 = ""
#     while n > 0:
#         n3 += str(n % 3)
#         n = n //3
#     return n3[::-1]
# def R(n):
#     n3 = troic(n)
#     if n % 3 == 0:
#         n3 += n3[-3:]
#     else:
#         n3 += troic((n % 3)*3)
#     return int(n3, 3)
#
# for n in range(1, 100):
#     if R(n) > 150:
#         print(n)

#ЗАДАНИЕ №8 - ТУТ ВООБЩЕ БЫЛИ РАЗНЫЕ ПРОТОТИПЫ ВСПОМНИТЕ ВСЕ
# from itertools import *
# cnt = 0
# for i in product("ПЯТНИЦА", repeat=5):
#     if i.count("Я") == 1 and i[0] != "Н":
#         cnt += 1
# print(cnt)


#ЗАДАНИЕ №9
# f = open("9.txt")
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = []
#     nepovt = []
#     for x in a:
#         if a.count(x) == 1:
#             nepovt.append(x)
#         else:
#             povt.append(x)
#     if len(nepovt) == 3 and len(set(povt)) == 2 and (sum(povt)/len(povt) < sum(nepovt)/len(nepovt)):
#         cnt += 1
# print(cnt)

#ЗАДАНИЕ №12
# for i in range(4, 10000):
# 	s = "5" + "2" * i
# 	while "52" in s or "1122" in s or "2222" in s:
# 		if "52" in s:
# 			s = s.replace("52", "11", 1)
# 		if "2222" in s:
# 			s = s.replace("2222", "5", 1)
# 		if "1122" in s:
# 			s = s.replace("1122", "25", 1)
# 	if (s.count("2") * 2 + s.count("5")*5 + s.count("1")*1) == 64:
# 		print(i)

#ЗАДАНИЕ №14
# for x in "0123456789ABCDE":
#     if (int("98" + x + "79641", 22) + int("25" + x + "49", 22) + int("63" + x + "5", 22)) % 21 == 0:
#         print(x, (int("98" + x + "79641", 22) + int("25" + x + "49", 22) + int("63" + x + "5", 22)) // 21)

#ЗАДАНИЕ №15
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((y + 3*x > A) or (x < 20) or (y < 50)) == False:
#                 break
#         if ((y + 3 * x > A) or (x < 20) or (y < 50)) == False:
#             break
#     else:
#         print(A)

#ЗАДАНИЕ №16
# import sys
# sys.setrecursionlimit(3000)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n - 1 + F(n - 1)
# print(F(2024) - F(2022))


#ЗАДАНИЕ №17
# f = open("17.7.txt")
# a = []
# for s in f:
#     a.append(int(s))
# all17 = []
# for x in a:
#     if str(x)[-2:] == "17":
#         all17.append(x)
# max17 = max(all17)
# sum_troyki = []
# for i in range(len(a) - 2):
#     if (((len(str(abs(a[i]))) == 3 and len(str(abs(a[i + 1]))) != 3 and len(str(abs(a[i + 2]))) != 3) or
#          (len(str(abs(a[i]))) != 3 and len(str(abs(a[i + 1]))) == 3 and len(str(abs(a[i + 2]))) != 3) or
#          (len(str(abs(a[i]))) != 3 and len(str(abs(a[i + 1]))) != 3 and len(str(abs(a[i + 2]))) == 3)) and
#             ((a[i] + a[i + 1] + a[i + 2]) < max17)):
#         sum_troyki.append(a[i] + a[i + 1] + a[i + 2])
# print(len(sum_troyki), max(sum_troyki))

#ЗАДАНИЕ №23
# def task23(start, end):
#     if start > end or start == 13:
#         return 0
#     if start == end:
#         return 1
#     return task23(start + 1, end) + task23(start + 2, end) + task23(start * 3, end)
# print(task23(3, 8) * task23(8, 18))

#ЗАДАНИЕ №24
# f = open("24.txt")
# s = f.readline()
# index_t = []
# for i in range(len(s)):
#     if s[i] == "T":
#         index_t.append(i)
# min_l = 10 ** 20
# for i in range(151, len(index_t)):
#     min_l = min(min_l, index_t[i] - index_t[i - 151])
# print(min_l - 1)

#ЗАДАНИЕ №25
# from fnmatch import *
# for x in range(2023, 10**8, 2023):
#     if fnmatch(str(x), "2*1?71"):
#         print(x, x // 2023)

#ЗАДАНИЕ №26
# f = open("26.3.txt")
# n, k = map(int, f.readline().split())
# data = []
# for s in f:
#     start, end = map(int, s.split())
#     data.append([end, start])
# data.sort()
# count_file, last_disk = 0, 0
# zal = 0
# podoshle = []
# for i in range(n):
#     if zal == 0:
#         zal = data[i][0]
#         podoshle.append(data[i])
#     elif zal <= data[i][1]:
#         zal = data[i][0]
#         podoshle.append(data[i])
# print(len(podoshle))
# print(podoshle)


#ЗАДАНИЕ №27А
# f = open('27_14a.txt')
# N = int(f.readline())
# k = int(f.readline())
# a = [int(s) for s in f]
# min_pr = 10**10
# for i in range(N):
#     for j in range(i + k, N):
#         for l in range(j + k, N):
#             min_pr = min(min_pr, a[i]*a[j]*a[l])
# print(min_pr)

#ЗАДАНИЕ №27Б
# f = open("27_3b.txt")
# n = int(f.readline())
# k = int(f.readline())
# a = []
# min1 = 10**10
# min2 = 10**10
# min_proiz = 10**10
# for s in f:
#     a.append(int(s))
# for i in range(2*k, len(a)):
#     min1 = min(min1, a[i - k - k])
#     min2 = min(min2, min1*a[i - k])
#     min_proiz = min(min_proiz, a[i]*min2)
# print(min_proiz)
