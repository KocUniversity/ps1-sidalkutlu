
n, B = list(map(int, input().strip().split()))
T = 5000

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

guess = 5000
low = 0
high = 10000
while True:
    if final_value*(guess-1) <= B and final_value*guess > B:
        T = guess
        break
    
    guess = (low + high)//2 


    if final_value*guess > B:
        high = guess
    else:
        low = guess



# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)