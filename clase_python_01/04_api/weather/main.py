from datetime import date
from weather.application.use_cases.get_weather import GetWeatherUseCase, GetWeatherRequest
from weather.infrastructure.adapters.open_weather_adapter import OpenWeatherAdapter
from weather.config import Config

def main():
    config = Config()
    weatheexr_service = OpenWeatherAdapter(config)
    use_case = GetWeatherUseCase(weather_service)

    ciudad = input("Ciudad: ").strip()
    fecha_str = input("Fecha (YYYY-MM-DD, vacío para hoy): ").strip()
    if fecha_str:
        try:
            forecast_date = date.fromisoformat(fecha_str)
        except ValueError:
            print("Fecha no válida. Usa el formato YYYY-MM-DD.")
            return
    else:
        forecast_date = date.today()

    request = GetWeatherRequest(city=ciudad, forecast_date=forecast_date)
    print(use_case.execute(request))

if __name__ == "__main__":
    main()