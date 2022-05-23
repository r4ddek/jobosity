# Jobsity SDET Challenge
Automation files for the contact form automation challenge. The project is written in `Python` and uses `Selenium` and `behave` frameworks. The tests are written in BDD, Gherkin notation and can be found in the `features` folder. For details on the implementation of the tests, please check the `steps` folder.

## 💻 Preconditions

Before you begin, make sure  `Python 3.8` or greater is installed.
* virtualenv is also required, please make sure you have it by opening a terminal and running
```
pip install virtualenv
```

## 🚀 Installing Dependencies and Running the Project

Before installing the dependencies, create and start a virtual environment:

1. Head over to the project root folder `jobosity`;
2. Create the virtualenv `virtualenv automation_project`
3. Start the virtualenv:
  
Linux and macOS:
```
source automation_project/Scripts/activate
```

Windows:
```
automation_project\Scripts\activate
```
You should see the name of your virtual environment in brackets on your terminal line e.g. (automation_project).

### ☕Installing Dependencies

To install the dependencies simply run

```
pip install -r requirements.txt
```



### 📫 Running the Project
Finally, to run the project do ```behave --junit``` in the root folder and it will start testing the scenarios. Once it has completed running you can either check the XML files in the `results` folder or check the terminal for the run details. Two out of seven scenarios are expected to FAIL.
