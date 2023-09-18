import read_csv as csv
import utils
import matplotlib.pyplot as plt

country = input('Country/Territory => ')
country = country.capitalize()
#print(country)

def run():
  data = csv.read_csv('./app/data.csv')
  dic_country = list(filter(lambda item: item['Country/Territory'] == country, data))
  dic_country = dic_country[0]
  #Hasta aqui funciona
  resultado = utils.population_by_dict_country(dic_country)
  return resultado

def generate_bar_chart(keys, values):
  fig, ax = plt.subplots() #figura y coordenadas
  ax.bar(keys, values, color='#FF81C0')
  plt.show()
if __name__ == '__main__': 
  keys = utils.separacion_keys(run())
  #print(keys)
  values = utils.separacion_values(run())
  #print(values)
  
  generate_bar_chart(keys, values)