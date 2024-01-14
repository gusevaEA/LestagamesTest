from collections import deque

class BufferDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(max_len=capacity)#переменная deque из модуля collections

    def empty_buff(self):
        return len(self.buffer) == 0

    def full_buff(self):
        return len(self.buffer) == self.capacity

    def enqueue(self, item):
        if self.full_buff():
            raise IndexError("Ошибка,Буффер полный")
        self.buffer.append(item) #добавляем в конец очереди

    def dequeue(self):
        if self.empty_buff():
            raise IndexError("Ошибка,Буффер пустой")
        return self.buffer.pop() #Метод pop автоматически возвращает значение по указанному индексу


#Плюсы второй реализации с deque из модуля collections:Вторая реализация, может работать с большим колличеством элементов, благодаря модулю автоматически обрабатывает индексы и головы и хвоста
#Минусы второй реализации  с deque из модуля collections: Вторая реализация напрямую зависит от модуля collections, может при работе по времени быть чуть с задержкой
