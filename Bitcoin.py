def bitcoin():  #Расчёт будущего баланса BTC и $ по годам и расчёт времени "Пенсии"
    print('input your amount of Bitcoin', end=': ')
    btc = float(input())

    btc_to_usd = 99 # курс BTC в тыс. долл. на 2024 год
    btc_to_usd_list = []
    # Считаем прогнозный кус по каждому году на ближайшие 16 лет (берём +24% каждый год):
    for _ in range(16):
        btc_to_usd_list.append(round(btc_to_usd, 2))
        btc_to_usd*=1.24

    print(btc_to_usd_list)
    # А это курсы в года Халвингов:
    halvings = [btc_to_usd_list[i] for i in range(16) if i % 4 == 0]
    print(halvings)
    # Твой баланс $ на каждый год:
    btc_to_usd_result = [btc*btc_to_usd_list[item] for item in range(16)]

    for year, dollars in enumerate(btc_to_usd_result, start=2024):
        print(f'year {year} : {dollars}')
    # Тут считаем когда можно брать деньги исходя из желания $
    print(f'let is calculate money to live')

    income = int(input('Dollars per month: ')) #Сколько нужно в месяц
    years = int(input('years: ')) #На протяжении скольки лет
    totally = (income * 12 * years)
    print('totally:', totally)
    start_year = 2024

    for i in range(16):
        if totally <= btc_to_usd_result[i] * 1000:
            print(f'Since {start_year} you can take, btc is {btc_to_usd_list[i]}K')
            print(f'your balance is ${btc_to_usd_result[i]}K')
            break
        start_year += 1

bitcoin()
