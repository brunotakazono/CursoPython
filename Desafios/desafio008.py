v = float(input('Digite um valor em (m): '))

cm = v * (10 ** 2)
mm = v * (10 ** 3)


print(f'O valor {v} convertido em centimetros é {cm:.0f} cm!', end=' ')
print(f'e convertido em milimetros é {mm:.0f} mm!')

