#https://openweathermap.org
#https://openweathermap.org/current
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
#criar uma conta no site, assim é possível obter uma key
import requests
def rodar():
    #ler o apikey.txt
    with open('apikey.txt', 'r') as arquivo:
        api_key = arquivo.read()

        #obtendo as variaveis
        cidade = input('\nDeseja saber o clima de qual cidade? ')
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic['weather'][0]['description']
        temp = requisicao_dic['main']['temp'] - 273.15

        #Função pra arredondar em duas casas a temperatura
        def arredondar(temp):
            return float( '%g' % ( temp ) )

        #print do resultado
        print(descricao, arredondar(temp),'ºC\n')

rodar()