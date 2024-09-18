while True:
    N = int(input("Введіть кількість елементів у масиві: "))
    if N >= 0:
        break
    else:
        print("Введіть інше додатнє число або 0.")

array = []

print(f"Введіть {N} елементів:")
for i in range(N):
    element = int(input())
    array.append(element)

reversed_array = array[::-1]
print("Масив у зворотному порядку:")
print(reversed_array)

