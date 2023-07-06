
def bank(X, Y):
    total = X  

    for i in range(Y):
        total += total * 0.1  

    return total
X = int(input('введите сумму вклада:'))  
Y = int(input('введите на сколько лет вклад (в годах):'))   

result = bank(X, Y)
print(result) 




