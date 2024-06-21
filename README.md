# PyBridge - Bridge to the other side

## Overview

PyBridge - Bridge to the other side, is a Python-based Event-Driven Script PyBridge (ESB) designed to facilitate the execution of scripts based on various triggers such as timers, schedules, or API calls. This project, based on Flask, is currently a work in progress.

## Features

- **Timer Intervals:** Execute scripts at regular intervals
- **Schedules:** Run scripts according to a predefined schedule
- **API Triggers:** Trigger script execution through API calls
- **Tokens:** Control execution rights

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.x
- Install the required dependencies listed below


### Installation

1. Clone the repository
```cmd
git clone https://github.com/thatsleepyman/PyBridge.git
```

2. Navigate to the project directory
```cmd
cd PyBridge
```

3. Install the required dependencies
```cmd
pip install -r requirements.txt
```
## Understanding Tokens
- **MASTER_TOKEN:** Acts like a license key, granting the requestor the right to send requests to PyBridge
- **PYROCESS_TOKEN:** Allows the requestor to send data to and trigger PyRocesses
  - Every PyRocess in every environment ``(main/ dev/ test)`` has their own separate PyRocess token
- **DEVELOPER_TOKEN:** Used by 'Developers' to trigger PyRocesses through the ``{ip}:{port}/PyBridge/dev/{PyRocess}`` routing
- **USER_TOKEN:** Used by 'Users' to trigger PyRocesses through the ``{ip}:{port}/PyBridge/main/{PyRocess}`` routing
- **TESTER_TOKEN:** Used by 'Testers' to trigger PyRocesses through the ``{ip}:{port}/PyBridge/test/{PyRocess}`` routing

## Note
PyBridge assumes that there is a **'.venv'** directory in the root directory of the project ('PyBridge/.venv'). Please create one and install the Python modules there. Once the '.venv' is placed in the root directory, you can move PyBridge anywhere you wish.

## License
This project is licensed under the MIT License - Feel free to use it as you wish, however some credit for this project would be nice if you end up using it ;)
