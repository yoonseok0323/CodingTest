n = int(input())
val = n//5
res = 0

if n % 5 == 0: # 5의 배수면 바로 몫을 구해서 최소한의 설탕 봉지 개수를 구함.
    res = val
else: # 5의 배수가 아니라면 
    for i in range(val, 0, -1): # 5로 나눈 몫이 가장 큰 수부터 1까지 확인 
        n2 = n - (5*i) 
        if n2 % 3 == 0: # 5로 나눈 나머지가 3의 배수라면   
                res = i + (n2//3) # 그 때의 몫과 5로 나눈 몫을 더해서 최소한의 설탕 봉지 개수를 구하고
                break # 반복문 빠져나옴.

    if n % 3 == 0 and res == 0: # 5로 나누면서 확인했지만 나머지가 한 번도 3의 배수가 아니었고, n이 3의 배수였을 경우
        res = n//3 # 3으로 나눈 몫이 최소한의 설탕 봉지 개수
    else: 
        if res == 0: # 아무조건도 해당되지 않는 경우
            res = -1

print(res)