*** Variables ***
${SINGAPORE_ID}       1c2531bf04f05ea6b5ea125ad3d852952d43f10dd7a21ddd4f220912986bab39c5d15d764e59f1f7833512baf78044e7

*** Settings ***
Test Timeout       300
Library         PlayerLibrary
Library         weather-info.py

Test Setup       Start Browser Then Open Url      https://weather.com/weather/tenday/l/${SINGAPORE_ID}     headless=True

Suite Teardown    Quit all browsers

*** Test Cases ***
USECASE_01 - Getting weather info of Singapore in 10 days
    [Tags]     ui    automated
    ${temperature_data}          Get all temperature data from ten days
    Save all the data to the file       ${temperature_data}
    Generate a summary report for the weather data       ${temperature_data}

