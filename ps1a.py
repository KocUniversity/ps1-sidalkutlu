
n, B = list(map(int, input().strip().split()))
T = 1

p_numbers = [0]

for i in range(1,n+1,1):
    if i % 2 == 0:
        p = ((2**i) + 1)
    else:
        p = ((3**i) + 1)
    p_numbers.append(p)

final_value = 0
for i in range(1,n+1):
        final_value += p_numbers[i]**(n-i)

while final_value*T <= B:
    T += 1


# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)
