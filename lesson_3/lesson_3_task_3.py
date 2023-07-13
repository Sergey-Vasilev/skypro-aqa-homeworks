from address import Address
from mailing import Mailing


to_address = Address(666666, "Нерюнгри", "Свободы", "10", "99")
from_address = Address(666677, "Екатеринбург", "Союзная", "40", "33")

mailing1 = Mailing(to_address, from_address, 500, 444444)
print("Отправление.трек№:{},из индекс:{}, город:{}, улица:{}, дом:{}, квартира:{}.В индекс:{}, город:{}, улица:{}, дом:{}, квартира:{}.Стоимость:{} рублей."
.format(mailing1.track,to_address.index, to_address.city, to_address.street, to_address.house, to_address.apartment,
          from_address.index, from_address.city, from_address.street, from_address.house, from_address.apartment,mailing1.cost))
              



           