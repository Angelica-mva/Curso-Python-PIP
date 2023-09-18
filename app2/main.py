import utils
import read_csv
import chart

def run():
  data = read_csv.read_csv('data.csv')
  country = input('type country => ')

  result = utils.population_by_country(data, country)
  
  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    chart.generate_bar_chart(country['Country/Territory'], labels, values)
    #chart.generate_pie_chart(labels, values)

if __name__ == '__main__': 
  run()
#si el archivo se esta ejecutando como script, __name__ será igual a '__main__', pero si el archivo se esta ejecutando desde otro scrip (o sea que el se esta usando como modulo) __name__ tomará el nombre del archivo que esta ejecutando o sea que será diferente de '__main__' entonces no se ejecutará el run