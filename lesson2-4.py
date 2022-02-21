u_string = input('Напишите Ваши любимые блюда: ').split()
for n, i in enumerate(u_string, 1):
    print(f'{n}. {i:.10}')
