"# onlineshop_pumpskill" 

В проекте onlineshop необходимо создать модель User - это таблица для хранения пользователей. Модель User должна содержать следующие поля:

name: поле строкового типа;
users_items: абстрактное описание связи с моделью UsersItem. Атрибут backref должен быть равен 'user'.
Необходимо создай модель UsersItem, со следующими полями:

user_id: внешний ключ - ссылка на модель User;
item_id: внешний ключ - ссылка на модель Item.
Добавить в модель User поле users_items - абстрактное описание связи с моделью UsersItem. Атрибут backref должен быть равен 'user'.

Добавь в модель Item поле users_items - абстрактное описание связи с моделью UsersItem. Атрибут backref должен быть равен 'item'.

Создать файл зависимостей requirements.txt и выложить проект на GitHub. Файл базы данных не должен версионироваться.


Запущенная версия проекта: https://immense-bastion-07139.herokuapp.com/