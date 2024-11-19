from matplotlib import pyplot as plt
import numpy as np

figure1 = plt.figure()
x1 = np.linspace(-10, 10, 30)
y1 = -x1 ** 2

axes_ = figure1.add_axes([0.1, 0.1, 0.9, 0.9])
axes_.plot(x1, y1, "mH-.")
axes_.plot(y1, x1, "cD-")

plt.ylabel('Y axis')
plt.xlabel('X axis')

axes_2 = figure1.add_axes([0.25, 0.25, 0.4, 0.4])
axes_2.plot(x1, np.sin(x1), "b--")
axes_2.plot(np.cos(x1), -x1, "g")
axes_2.grid(True, color="k")

fig, ax = plt.subplots()

languages = ['English', 'Mandarin', 'Hindi', 'Spanish', 'French']
speakers = [1132, 1117, 615, 534, 280]

ax.pie(speakers, labels=languages, autopct='%.1f%%', shadow=True,
       colors=['y', 'm', 'c', 'g', 'b'],
       wedgeprops={'linewidth': 2.0, 'edgecolor': 'lightgrey'})

ax.axis('equal')
ax.set_title('Top 5 most spoken languages in the world')
plt.legend()
plt.show()
