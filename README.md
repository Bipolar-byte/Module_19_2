Открываем Django shell:
python manage.py shell

Создаём покупателей (Buyer) через QuerySet:

from task1.models import Buyer, Game


buyer1 = Buyer.objects.create(name="Иван", balance=5000.00, age=25)  # Взрослый
buyer2 = Buyer.objects.create(name="Петр", balance=3000.00, age=17)  # Несовершеннолетний
buyer3 = Buyer.objects.create(name="Алексей", balance=7000.00, age=30)  # Взрослый

Создаём игры (Game) через QuerySet:


game1 = Game.objects.create(title="Cyberpunk 2077", cost=2499.99, size=50.0, 
                            description="Игра в открытом мире", age_limited=True)

game2 = Game.objects.create(title="Minecraft", cost=999.99, size=2.0, 
                            description="Кубический мир без границ", age_limited=False)  # Без возрастного ограничения

game3 = Game.objects.create(title="GTA V", cost=1999.99, size=60.0, 
                            description="Гангстерский боевик", age_limited=True)

Назначаем игры покупателям через QuerySet (set())


buyer1.games.set(Game.objects.all())


buyer2.games.set(Game.objects.filter(age_limited=False))


buyer3.games.set(Game.objects.filter(age_limited=True))
Проверка результата через QuerySet

print("Игры у Ивана:", list(Buyer.objects.get(name="Иван").games.values_list("title", flat=True)))
print("Игры у Петра:", list(Buyer.objects.get(name="Петр").games.values_list("title", flat=True)))
print("Игры у Алексея:", list(Buyer.objects.get(name="Алексей").games.values_list("title", flat=True)))
