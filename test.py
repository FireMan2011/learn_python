# for i in range(5): print("Hello world!")

# n = int( input() )
# n = int( input() )


# print(n*20/5)
# print(n*20)
# print(n*2.0)



# -----------------------------
# розрахунки
# -----------------------------

print("Введіть початкове число")
start_number = int(input())
print("Ви ввели число: " + str(start_number))
print("")

print("Введіть число зменшення")
reduce_number = int(input())
print("Початкове число буде зменшуватись на: " + str(reduce_number))
print("")

count = 0
result = start_number

while result >= 0:
    # count = count + 1
    count += 1
    # result = result - reduce_number
    result -= int(reduce_number)


print("Було виконано ітерацій: " + str(count))
print("Отримали від'ємне число' " + str(result))












