We are using Selenium Hybrid Framework
(Python , Pytest , Html Reports , Selenium ,Page Object Model )

Step 1
Install Pycharm and download Python on your system
Create a new project
Install these packages
Selenium (Libraries )
pytest (Unit test framework)
pytest-html (used for html reports)
pytest-xdist  (run test suites )

Step 2
Folder Structure
pageObjects (package)
testCases (package)
utilities (package)
Test Data (Folder)
Configuration (Folder)
Logs (Folder)
Screenshot (Folder)
Reports (Folder)

Step 3
Download Selenium Driver exe file from the below website
https://chromedriver.chromium.org/downloads

Step 4
Open the testCases Folder
Open Confest.py file
Cope the chromedriver path and pass the path to driver variable

Step 5
Once all dependencies are complete
Open the terminal in pycharm
Write this command ( pytest -s -v testCases/test_HomePage.py )
Press Enter
