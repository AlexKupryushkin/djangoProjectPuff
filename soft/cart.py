from django.utils.safestring import mark_safe

from .models import Divan


class DivanCart:
    key = "cart"
    divan_image = '<img height="40px" src="/static/soft/img/111.png">'

    def __init__(self, request):
        """
        Инициализируем корзину
        """

        # request.session - хранилище данных пользователя
        # создаем свой объект
        self.session = request.session

        # Смотрим корзину пользователя self.session.get("cart")
        cart = self.session.get(self.key)
        if not cart:
            # Если её еще нет.
            # Создаем корзину.
            cart = self.session[self.key] = {}
            # Создаем список заказов
            self.session["orders"] = []

        # Корзина
        self.cart = cart
        print(cart)

        # Будущий список диванов
        self.divans = []

    def add(self, divan: Divan, quantity=1, update_quantity=False,):
        """
        Добавить продукт в корзину или обновить его количество.
        """

        divan_id = str(divan.id)
        if divan_id not in self.cart:
            self.cart[divan_id] = {"quantity": 0}
        if update_quantity:
            self.cart[divan_id]["quantity"] = quantity
        else:
            self.cart[divan_id]["quantity"] += quantity

        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[self.key] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, divan):
        """
        Удаление товара из корзины.
        """
        divan_id = str(divan.id)
        if divan_id in self.cart:
            del self.cart[divan_id]
            self.save()

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item["quantity"] for item in self.cart.values())

    def total_count(self):
        return len(self)

    def total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        if not self.divans:
            self.create_objects()
        price = 0
        for divan in self.divans:
            price += divan.total_cost
        return price

    def clear(self):
        # удаление корзины из сессии
        del self.session[self.key]
        self.session.modified = True

    def create_objects(self):
        self.divans = []
        divans = Divan.objects.filter(id__in=list(map(int, self.cart.keys())))
        for divan in divans:
            divan: divan

            # СОЗДАЕМ СВОИ АТРИБУТЫ ДЛЯ ОБЪЕКТОВ ДИВАНОВ
            divan.count = self.cart[str(divan.id)]["quantity"]
            # картинки
            divan.count_images = mark_safe(self.divan_image * divan.count)

            divan.total_cost = divan.count * divan.cost
            self.divans.append(divan)
        return self
