import matplotlib.pyplot as pyplot

labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
pyplot.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=105, counterclock=False)
pyplot.show()