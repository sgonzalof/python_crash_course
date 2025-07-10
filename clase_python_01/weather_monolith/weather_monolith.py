import requests
from datetime import date

API_KEY = "TU_API_KEY_AQUI"  # Pon aquí tu clave real de OpenWeather

def get_weather(city, forecast_date):
    url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'es'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        for forecast in data['list']:
            forecast_date_str = forecast['dt_txt'].split()[0]
            if forecast_date_str == forecast_date.isoformat():
                temp = forecast['main']['temp']
                desc = forecast['weather'][0]['description']
                humidity = forecast['main']['humidity']
                city_name = data['city']['name']
                return (
                    f"El tiempo en {city_name} será de {int(temp)} grados, "
                    f"con {desc} y {humidity}% de humedad"
                )
        return f"No hay pronóstico disponible para {forecast_date}"
    except Exception as e:
        return f"Error al obtener el pronóstico: {e}"

def main():
    city = input("Ciudad: ").strip()
    fecha_str = input("Fecha (YYYY-MM-DD, vacío para hoy): ").strip()
    if fecha_str:
        try:
            forecast_date = date.fromisoformat(fecha_str)
        except ValueError:
            print("Fecha no válida. Usa el formato YYYY-MM-DD.")
            return
    else:
        forecast_date = date.today()
    print(get_weather(city, forecast_date))

if __name__ == "__main__":
    main()