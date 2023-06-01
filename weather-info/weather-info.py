from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn as Robot

context = Robot().get_library_instance('PlayerLibrary')


@keyword("Get all temperature data from ten days")
def get_all_temperature_data_from_ten_days():
    ten_day_data = []
    rows = context.get_elements('//*[@data-testid="ExpandedDetailsCard"]')
    for i in range(1, len(rows)):
        date = rows[i].locator('xpath=.//*[@data-testid="daypartName"]').inner_text()
        high_tem = rows[i].locator('xpath=.//*[@data-testid="TemperatureValue"][contains(@class,"high")]').inner_text()
        low_tem = rows[i].locator('xpath=.//*[@data-testid="TemperatureValue"][contains(@class,"low")]').inner_text()
        description = rows[i].locator('xpath=.//span[contains(@class,"DetailsSummary--extendedData")]').inner_text()
        humidity_day = rows[i].locator('xpath=.//*[@data-testid="HumiditySection"]//*[@data-testid="PercentageValue"]').nth('0').text_content()
        humidity_night = rows[i].locator('xpath=.//*[@data-testid="HumiditySection"]//*[@data-testid="PercentageValue"]').nth('1').text_content()
        row_data = {"date": date,
                    "high_tem": high_tem,
                    "low_tem": low_tem,
                    "description": description,
                    "humidity_day": humidity_day,
                    "humidity_night": humidity_night
                    }
        ten_day_data.append(row_data)
    return ten_day_data


@keyword("Save all the data to the file")
def save_all_the_data_to_the_file(data, file_name="weather-data.txt"):
    with open(file_name, "w", encoding='utf8') as f:
        print(*data, sep="\n", file=f)


@keyword("Generate a summary report for the weather data")
def generate_a_summary_report_for_the_weather_data(data):
    highest_tem_day = max(data, key=lambda obj: obj['high_tem'])
    lowest_tem_day = min(data, key=lambda obj: obj['low_tem'])
    highest_humidity_day = max(data, key=lambda obj: obj['humidity_day'])
    lowest_humidity_day = min(data, key=lambda obj: obj['humidity_day'])
    highest_humidity_night = max(data, key=lambda obj: obj['humidity_night'])
    lowest_humidity_night = min(data, key=lambda obj: obj['humidity_night'])
    statistic_data = {
        "HIGHEST TEMPERATURE": highest_tem_day["high_tem"],
        "HIGHEST TEMPERATURE DATE": highest_tem_day["date"],
        "LOWEST TEMPERATURE": lowest_tem_day["low_tem"],
        "LOWEST TEMPERATURE DATE": lowest_tem_day["date"],
        "HIGHEST HUMIDITY DAY": highest_humidity_day["humidity_day"],
        "HIGHEST HUMIDITY DAY ON DATE": highest_humidity_day["date"],
        "LOWEST HUMIDITY DAY": lowest_humidity_day["humidity_day"],
        "LOWEST HUMIDITY DAY ON DATE": lowest_humidity_day["date"],
        "HIGHEST HUMIDITY NIGHT": highest_humidity_night["humidity_night"],
        "HIGHEST HUMIDITY NIGHT ON DATE": highest_humidity_night["date"],
        "LOWEST HUMIDITY NIGHT": lowest_humidity_night["humidity_night"],
        "LOWEST HUMIDITY NIGHT ON DATE": lowest_humidity_night["date"],
    }
    save_all_the_data_to_the_file([(key, value) for key, value in statistic_data.items()], "summary-report.txt")