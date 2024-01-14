class C_Buffer:
    def __init__(self, capacity): #инициализация класса
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def empty_buff(self):
        return self.size == 0 #проверка очереди на то, пустая она или нет

    def full_buff(self):
        return self.size == self.capacity #проверка очереди полная она или нет

    def enqueue(self, item):
        if self.full_buff():
            raise IndexError("Буффер переполнен")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity #узнаем индекс последнего элемента
        self.size += 1

    def dequeue(self):
        if self.empty_buff():
            raise IndexError("Буффер пустой")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity #узнаем индекс первого элемента
        self.size -= 1
        return item

#Сложность (худший случай) О(1)
#Плюсы первой реализации:Первая реализация очень доступна и понятна, она работает без внешних модулей, а значит по времени будет чуть быстрее
#Минусы первой реализации:Первая реализация плоха тем, что с большим колличеством элементов будет тяжело работать