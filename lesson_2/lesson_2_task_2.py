def is_year_leap(y):
    if  y % 4 == 0:
        return True
    elif y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 != 0:
        return False


y = int(input('Введите год : '))
res = is_year_leap(y)

if res:
     print(f"Год {y}: True")
elif not res:
     print(f"Год {y}: False") 