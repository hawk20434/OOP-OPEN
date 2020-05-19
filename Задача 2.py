from abc import ABC, abstractmethod

class Hero:
    def __init__(self, opit, lvl):
        self.stats = {
            "HP": 10,
            "MP": 20,
            "SP": 30,
        }
        self.opit=opit
        self.lvl=lvl
    def opit_up(self):
        self.opit += 10
        return self.opit
    def lvl_up(self):
        stats = self.get_stats()
        self.lvl += 1
        stats["HP"] += 10
        stats["MP"] += 10
        stats["SP"] += 10
        return self.lvl, 'уровень', stats
    def get_stats(self):
        return self.stats.copy()
    def can(self):
        if Mag.opit >= 20:
            print("Новый уровень!", Mag.lvl_up())
            ach.subscribe(popeda)
            ach.notify("Победа!победа! вместо обеда!")
            print(popeda.achievements)
        elif Mag.opit < 20:
            print("Нужно больше опыта милорд!")
        return "ВПЕРЕД К ПОБЕДЕ!"




class ObservableEngine():
    def __init__(self):
        self.__subscribers = set()
    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)
    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)
    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()
    def update(self, message):
        self.achievements.add(message)


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()
    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)


ach = ObservableEngine()
popeda = FullNotificationPrinter()
Mag = Hero(0, 1)
print("Вы выбрали героя: Маг Саруман!")
print("Его показатели на начальном уровне!", Mag.get_stats())
print("------------")
print("Вы выиграли сражение!")

print("------------")

print(Mag.lvl, "- уровень")
print(Mag.can())
print("Ваш опыт: ", Mag.opit_up())

print("------------")

print(Mag.lvl, "- уровень")
print(Mag.can())
print("Ваш опыт: ", Mag.opit_up())
print(Mag.can())