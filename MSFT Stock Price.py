import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconverter


fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

x, y = np.loadtxt('daily_adjusted_MSFT.csv', delimiter=',', unpack=True, converters={0: bytespdate2num('%Y-%m-%d')})

ax1.plot_date(x, y, '-', label='Price')
ax1.plot([], [], linewidth=4, label='loss', color='red', alpha=1)
ax1.plot([], [], linewidth=4, label='gain', color='green', alpha=1)
ax1.axhline(y[22], color='orange', linewidth=1)
ax1.fill_between(x, y, y[22], where=(y > y[22]), facecolor='g', alpha=1)
ax1.fill_between(x, y, y[22], where=(y < y[22]), facecolor='r', alpha=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(35)
ax1.grid(True)

ax1.tick_params(axis='x', colors='#f06215', size=1, labelsize=6)

plt.plot(x, y, label='Loaded from file!', color='pink')
plt.xlabel('Date', color='blue')
plt.ylabel('Price', color='blue')
plt.title('Microsoft Stock Performance - 2019')
plt.legend()
plt.show()
