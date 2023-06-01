# singapore-weather-information
**Prerequisites:**
1. Install Python 3.10 
2. IDE: IntelliJ or Pycharm
3. IDE Plugins: 
   1. Robot Framework Language Server
   2. Python Community Edition
4. Install all the libraries in the `requirement.txt` file
   1. Using command `pip install -r requirement.txt` to install them.
   2. Make sure you install them to correct project interpreter’s folder

**Quick guides:**
- Test cases are stored in `weather-info.robot` file
- When everything is good to go, using below command to run your first testcase:
      ```robot --loglevel TRACE -d results {path_to_the_robot_file}```
  - E.g:```robot --loglevel TRACE -d results C:\GitHub\the-weather-info\weather-info\weather-info.robot```
- After finishing the execution, some output files will be generated in `results` folder:
  - output.xml
  - log.xml
  - report.html
- Also some reports will be generated accordingly:
    - summary-report.txt
    - weather-data.txt