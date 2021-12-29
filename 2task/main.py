import numpy as np
import random

def model():
    n_packets = 1000
# Текущее время
    t = 0
# текущий размер очереди
    queue = 0
# Интесивность входного потока
    lambda_day = 1
# Максимальный размер очереди
    m = 7
# Интенсивность выходного потока
    mu = 2
# время, когда прибор освободится
    t_free = 0
# Количество потярянных пактеов
    n_lost = 0
    for i in range(n_packets):
# время поступления нового пакета
        t += np.random.exponential(scale=1/lambda_day)
# проверяем есть, ли очередь
        if queue>0:
            while t_free < t and queue > 0:
# обрабатываем пакеты из очереди до момента t
                t_free += np.random.exponential(scale=1/mu)
                queue -= 1
# проверяем, свободен ли концентратор
        if t_free < t:
# Концентратор свободен, определяем время обслуживания
            t_free = t + np.random.exponential(scale=1/mu)
        else:
# Концентратор занят
            if queue < m:
# ставим пакет в очередь
                queue += 1
            else:

# пакет теряется
                n_lost += 1
#print('потеряно '+str(n_lost)+' из '+str(n_packets))
    return n_lost/n_packets

def main():
    # Инициализация генеротора случайных чисел
    np.random.seed(100)
    # Количество повторов в методе Монте-Карло
    n_rep = 1000
    # Вероятность блокировки
    p_refuse = 0
    # Имитационное моделирование
    for i in range(n_rep):
        p_refuse += model()
    # Оценка вероятности блокировки
    p_refuse /= n_rep
    print('average probability = '+str(p_refuse))

if __name__ == "__main__":
    main()