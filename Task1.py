def isEven(value):
    return value % 2 == 0 #исходный вариант

def isEven(value):
    return (value & 1) == 0 #побитовая операция,более быстрый способ, чем с оператором % так как у & приоритет в выполнении

