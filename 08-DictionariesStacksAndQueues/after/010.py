import stack as st

number = int(input("Give a number: "))
counter = 0

while number > 0:
    counter += 1
    if number%2:
        st.push(1)
    else:
        st.push(0)
    number = int(number/2)

    if number == 1:
        counter += 1
        st.push(1)
        break

arr = []

for i in range(counter):
    arr.append(st.pop())

print("Binary number: ", end="")
for i in arr:
    print(i, end="")