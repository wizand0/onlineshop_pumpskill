from app import db
from app.models import Brand, Item


fake_data = [
    {'title': 'Kia',
     'items': [{'title': 'Товар 3 бренда Kia', 'price': 10, },
               {'title': 'Товар 4 бренда Kia', 'price': 20, },
               {'title': 'Товар 5 бренда Kia', 'price': 30, },
               {'title': 'Товар 6 бренда Kia', 'price': 40, }, ]
     },
    {'title': 'VW',
     'items': [{'title': 'Товар 4 бренда VW', 'price': 100, },
               {'title': 'Товар 3 бренда VW', 'price': 200, }, ]
     },
    {'title': 'Haval',
     'items': [{'title': 'Товар 4 бренда Haval', 'price': 1000, },
               {'title': 'Товар 6 бренда Haval', 'price': 2000, },
               {'title': 'Товар 5 бренда Haval', 'price': 3000, }, ]
     },
]

for brand in fake_data:
    new_brand = Brand(title=brand['title'])
    db.session.add(new_brand)

    for item in brand['items']:
        new_item = Item()
        new_item.title = item['title']
        new_item.price = item['price']
        new_item.brand = new_brand
        db.session.add(new_item)

db.session.commit()
