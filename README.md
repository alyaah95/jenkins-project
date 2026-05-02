🚀 jenkins-project
📋 Project Overview
This project demonstrates a complete CI/CD Pipeline using Jenkins and WSL2. It automates the lifecycle of a Data Engineering micro-service, from environment setup to testing and containerization simulation. This task was completed as part of the Data Engineering Track at ITI.

🛠️ Tech Stack
OS: Ubuntu (WSL2)

Automation: Jenkins (Pipeline as Code)

Language: Python 3.12

Testing: Pytest

Environment Management: Python Virtual Environments (venv)

🏗️ Pipeline Stages
The pipeline follows a structured automation flow:

Build Stage:

Creates a clean Python Virtual Environment.

Installs necessary dependencies (pytest) without affecting the system-wide Python installation.

Test Stage:

Executes automated unit tests for the processor.py logic.

Ensures data formatting is correct before deployment.

Deploy as Container (Simulation):

Prepares for Docker image building.

Logs the deployment status of the my-jenkins-app:v1 .

⚙️ How to Run Locally
Clone this repository.

Ensure you have Java 21 and Python 3.12 installed on your WSL.

Run Jenkins: java -jar jenkins.war.

Create a new "Pipeline" project and point it to the provided Jenkinsfile.
