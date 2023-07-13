from smartphone import Smartphone

cantalog = []


smartphone1 = Smartphone('Apple', 'iPhone 13 Pro', '+79991234567')
smartphone2 = Smartphone('Samsung', 'Galaxy S21 Ultra', '+79001234568')
smartphone3 = Smartphone('Huawei', 'P40 Pro', '+79111234569')
smartphone4 = Smartphone('Xiaomi', 'Mi 11', '+79871234570')
smartphone5 = Smartphone('OPPO', 'Reno 5', '+79551234571')


cantalog.append(smartphone1)
cantalog.append(smartphone2)
cantalog.append(smartphone3)
cantalog.append(smartphone4)
cantalog.append(smartphone5)


for smartphone in cantalog:
    print('<Марка> -{}.  <Модель> -{}.  <Номер телефона>: {}.'.format(smartphone.brand, smartphone.model, smartphone.number))
    