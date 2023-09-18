import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots() #figura y coordenadas
  ax.bar(labels, values, color='#FF81C0')
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots() 
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

def generate_plot_chart(labels, values):
  fig, ax = plt.subplots() 
  ax.plot(labels, values, marker = 'o')
  ax.set_title('line')
  plt.show()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 0, 800]
  
  generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
  #generate_plot_chart(labels, values)