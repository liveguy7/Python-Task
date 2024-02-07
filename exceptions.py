
def kelvinToFahrenheit(temp):
  try:
    assert(temp >= 0), temp
    return((temp - 273) * 1.8) + 32
  except AssertionError as a:
    print('colder than absolute zero', a.args)

print(kelvinToFahrenheit(273), 'degrees fahrenheit')
print(kelvinToFahrenheit(505.78), 'degrees fahrenheit')
print(kelvinToFahrenheit(-5), 'degrees fahrenheit')

