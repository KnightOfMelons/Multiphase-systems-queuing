# Домашнее задание № 6

# Ввиду сложности возникшей аварийной ситуации в электрической сети на ее устранение были направлены
# оперативно-выездная бригада и две ремонтные бригады электромонтеров. Интенсивность потока отключений электрической
# сети λ = 0,2, среднее время подготовки к ремонту tподг = [0,5, 4] ч, среднее время ремонта tобсл = [1, 5] ч.
# Определить вероятности состояний и показатели эффективности СМО, построить графики Q, A, kзан.

import numpy as np
import matplotlib.pyplot as plt

num_channels = 3
arrival_rate = 0.2

t_prep, t_serv = np.meshgrid(np.linspace(0.5, 4, 100), np.linspace(1, 5, 100))

mu1 = 1 / t_prep
mu2 = 1 / t_serv

mu = mu2 * mu1 / (mu1 + mu2)

y = arrival_rate / mu

prob_p0 = (1 + y / 1 + y ** 2 / 2) ** (-1)
block_probability = y ** 2 / 2 * prob_p0
throughput_ratio = 1 - block_probability
effective_arrival_rate = arrival_rate * throughput_ratio
avg_busy_channels = effective_arrival_rate / mu

parameters = {
    'Относительная пропускная способность': ('Q', throughput_ratio),
    'Абсолютная пропускная способность': ('A', effective_arrival_rate),
    'Среднее число занятых каналов': ('k_зан', avg_busy_channels)
}

cmaps = ['viridis', 'plasma', 'cividis']

# Не знаю какие ещё графики здесь выводить, но сделал так
for i, (name, (label, value)) in enumerate(parameters.items()):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(t_prep, t_serv, value, cmap=cmaps[i % len(cmaps)])
    ax.set_title(name)
    ax.set_xlabel('Время подготовки (t_подг)')
    ax.set_ylabel('Время обслуживания (t_обсл)')
    ax.set_zlabel(label)
    plt.show()
