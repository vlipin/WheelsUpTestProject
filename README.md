# Test-Project

This is test project for automation coverage (functional and non-functional) of sample test project.

#Configuration
Before running tests PyCharm should be installed (light-weight Community edition is enough). Also:
  - Install python (2.7 is fine)
  - Install pip: 'sudo easy_install pip' in Terminal
  - Install nose: 'sudo pip install nose' or 'sudo easy_install nose'
  - Install selenium: 'sudo pip install selenium'
  - Install requests library: 'sudo pip install requests'
  
Two test suites are available: test_api_calls.py (API and data tests) and test_ui_wheelsup_scenario.py (Functional tests)

#Running of tests
To run tests suite you need to specify in terminal file name of it in command (running in root framework folder):
#### nosetests -v -s --nologcapture ./tests/test_api_calls.py
#### nosetests -v -s --nologcapture ./tests/test_ui_wheelsup_scenario.py

#Shell script
To run shell script which is creating 7 files and remove 4 first, go to /MyFiles
folder and execute:
#### sh simple_shell_script.sh

