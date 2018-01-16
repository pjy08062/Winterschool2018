sec=20000
min=sec//60
time1=min//60
min=min%60
remainder=20000%60
print(sec,'또는',time1,'시간',min,'분',remainder,'초')
