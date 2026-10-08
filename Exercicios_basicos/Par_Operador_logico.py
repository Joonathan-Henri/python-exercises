temperatura = float(input('Digite a temperatura para classificar: '))

if temperatura >= 35:
    print(f'temperatura de {temperatura}°C: Muito quente')
elif temperatura >= 25:
    print(f'ftemperatura de {temperatura}°C: Agradável')
elif temperatura >= 15:
    print(f'temperatura de {temperatura}°C: Fresco')
else:
    print(f'temperatura de {temperatura}°C: Muito frio')
