print('Reloj digital desde las 00:00:00 hasta las 23:59:59')
seg,min,hour=0,0,0
while hour!=23 or min!=59 or seg!=59:
    if seg==60:
        seg=0
        min+=1
    elif min==60:
        min=0
        hour+=1 
    else:
        seg+=1
    if hour in range(0,10) and min in range(0,10) and seg in range(0,10):
        print(f'La hora es: 0{hour}:0{min}:0{seg}')
    elif hour in range(0,10) and min in range(0,10) and seg not in range(0,10):
        print(f'La hora es: 0{hour}:0{min}:{seg}')
    elif  hour in range(0,10) and min not in range(0,10) and seg not in range(0,10):
        print(f'La hora es: 0{hour}:{min}:{seg}')
    elif  hour in range(0,10) and min not in range(0,10) and seg in range(0,10):
        print(f'La hora es: 0{hour}:{min}:0{seg}')
    elif  hour not in range(0,10) and min in range(0,10) and seg in range(0,10):
        print(f'La hora es: {hour}:0{min}:0{seg}')
    elif  hour not in range(0,10) and min in range(0,10) and seg not in range(0,10):
        print(f'La hora es: {hour}:0{min}:{seg}')
    elif  hour not in range(0,10) and min not in range(0,10) and seg in range(0,10):
        print(f'La hora es: {hour}:{min}:0{seg}')
    else: 
        print(f'La hora es: {hour}:{min}:{seg}')
        