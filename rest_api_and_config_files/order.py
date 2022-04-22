# * Напечатайте номер заказа
# * Напечатайте адрес отправки
# * Напечатайте описание посылки, ее стоимость и кол-во
# * Сконвертируйте yaml файл в json
# * Создайте свой yaml файл -> файл example_yaml.yaml
import yaml
import json


with open('order.yaml') as f:
    order_data = yaml.safe_load(f)

print(f'Номер заказа: {order_data["invoice"]}')
print(f"Адрес доставки: {order_data['bill-to']['address']['lines']}")
for product in order_data['product']:
    print(f"Описание продукта: {product['description']}")
    print(f"Цена: {product['price']}")
    print(f"Количество: {product['quantity']}")
    print('-----------------------')

with open("order.json", "w") as f:
    json.dump(order_data, f, default=str)
