from .factory import Factory
from .item import Item
from .employee import Worker
from .factory import Factory

def run():
    worker1 = Worker(name="Abdoul", job="CEO", years=10, factory_pk= 1)
    # print(worker1.dbpath)
    worker1.save()
    worker1.set_department("Tech")
    worker1.save()

    worker2 = Worker(name="Sam", job="Software engineer", years=5, factory_pk= 1)
    worker2.save()

    item1 = Item(name="piano", explosive=True, weight=2.5, cost=2000.0, factory_pk=1)
    item1.save()
    item1.explode()

    item2 = Item(name="Guitar", explosive=False, weight=1.5, cost=2500.0, factory_pk=2)
    item2.save()
    item2.explode()

    factory1 = Factory(name="APC")
    factory1.save()
    factory1.get_products()
    factory1.get_workers()

    factory1.add_day()
    factory1.save()

