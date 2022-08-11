#https://openweathermap.org
#https://openweathermap.org/current
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
#criar uma conta no site, assim é possível obter uma key
import requests

API_key = "colar a key aqui"
link = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"