import matplotlib.pyplot as plt
import config


for a, b in list(config.dict_faces.items())[:10]:
    plt.text(a, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=11)  # ha Текст указывается в середине столбца, va указывает положение текста, а fontsize указывает размер шрифта

# Установить данные по осям X и Y, оба могут быть списком или кортежем
x_axis = tuple(list(config.dict_faces.keys())[:10])
y_axis = tuple(list(config.dict_faces.values())[:10])

plt.bar(x_axis, y_axis)  # Если цвет не указан, все столбцы будут одного цвета

# plt.xlabel("Люди")  # Укажите описание информации по оси X
plt.ylabel("Количество")  # Укажите информацию описания оси Y
plt.title('Статистика появления лиц на фото')  # Укажите информацию описания диаграммы
plt.ylim(0, 200)  # Укажите высоту оси Y
plt.savefig('images/{}.png'.format('faces1'))  # Сохранить как картинку
plt.show()

for a, b in list(config.dict_faces.items())[10:]:
    plt.text(a, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=11)

x_axis2 = tuple(list(config.dict_faces.keys())[10:])
y_axis2 = tuple(list(config.dict_faces.values())[10:])

plt.bar(x_axis2, y_axis2)  # Если цвет не указан, все столбцы будут одного цвета

# plt.xlabel("Люди")  # Укажите описание информации по оси X
plt.ylabel("Количество")  # Укажите информацию описания оси Y
plt.title('Статистика появления лиц на фото')  # Укажите информацию описания диаграммы
plt.ylim(0, 200)  # Укажите высоту оси Y
plt.savefig('images/{}.png'.format('faces2'))  # Сохранить как картинку
plt.show()
