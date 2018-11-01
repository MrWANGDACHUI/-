ability=1
b=1
days=365
while b<=days:
    if b<=3:
        ability=1
    elif b>3:
        ability=ability*(1+0.01)
    b=b+1
    print(ability)
