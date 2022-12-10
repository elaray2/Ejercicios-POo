#Ejercicio 01
import random
texto = 'afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood'
contador = 0
while contador < 20:
    inicio = random.randrange(int(len(texto))-10)
    rango = random.randrange(3,10)
    final = inicio + rango
    cadena = texto[inicio:final]
    rev = ''.join(reversed(cadena))
    if (cadena == rev):
        print(cadena)
        texto = texto.replace(cadena,'')
        contador +=1
