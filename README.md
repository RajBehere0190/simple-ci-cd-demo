# simple-ci-cd-demo

# Area Calculation Application with CI/CD Integration

## Project Overview

This project demonstrates how to implement a simple Python script for area calculations of geometric shapes (square, circle, triangle) with unit testing. The script is integrated into a CI/CD pipeline using GitHub Actions. Every code push triggers automated tests to ensure the correctness of the functionality.


- **.github/workflows/ci-cd-pipeline.yml**: Defines the GitHub Actions workflow to automatically build, test, and deploy the application.
- **app.py**: Contains the Python code for calculating areas of different shapes and the corresponding unit tests.
- **requirements.txt**: Lists the dependencies needed for the application, like `pytest` for testing.
- **README.md**: Provides an overview of the project, installation instructions, and setup guidelines.

## Prerequisites

Before you can run the application or set up the CI/CD pipeline, make sure you meet the following requirements:

| Requirement        | Details                                                                 |
|--------------------|-------------------------------------------------------------------------|
| Python             | Version 3.6 or higher must be installed on the machine.                  |
| GitHub Account     | A GitHub repository must be available to push code and integrate GitHub Actions. |
| GitHub Actions     | CI/CD is configured through a `.github/workflows/` directory containing a YAML file. |
| Basic Knowledge    | Understanding of Python basics (functions, dictionaries, exception handling). |
| Text Editor/IDE    | (Optional) VS Code, PyCharm, or any preferred text editor to edit Python files. |
| Internet Connection| Required to push code to GitHub and trigger GitHub Actions.              |

## Setup Instructions

1. **Clone the Repository**  
   Clone this repository to your local machine:


   (`git clone https://github.com/yourusername/simple-ci-cd-demo.git`)

2. **Install Dependencies**
Make sure you have Python 3.6 or higher. Install the required dependencies using:

    (`pip install -r requirements.txt`)

3. **Run the Application**
To manually run the script and calculate areas for a square, circle, and triangle, execute:

    (`python app.py`)

4. **CI/CD Pipeline**
The GitHub Actions pipeline is already configured. When you push changes to the repository, GitHub Actions will automatically:

    Run unit tests defined in app.py

    Notify you if any test fails


## How It Works in the CI/CD Pipeline
Code is pushed to GitHub.

GitHub Actions automatically triggers the CI/CD pipeline defined in .github/workflows/ci-cd-pipeline.yml.

The tests in test_calculate_area() function are executed.

If all tests pass, the build succeeds.

If any test fails, the build fails, and developers are alerted.
