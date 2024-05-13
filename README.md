# Bowser_the_Pyrocess_Browser

## Overview

Bowser_the_Pyrocess_Browser is a Python-based Event-Driven Script Browser (ESB) designed to facilitate the execution of scripts based on various triggers such as timers, schedules, or API calls. This project, based on Flask, is currently a work in progress.

## Features

- **Timer Intervals:** Execute scripts at regular intervals.
- **Schedules:** Run scripts according to a predefined schedule.
- **API Triggers:** Trigger script execution through API calls.
- **Tokens:** Control execution rights.

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.x
- Install the required dependencies listed below


### Installation

1. Clone the repository
```cmd
git clone https://github.com/thatsleepyman/Bowser_the_Pyrocess_Browser.git
```

2. Navigate to the project directory
```cmd
cd Bowser_the_Pyrocess_Browser
```

3. Install the required dependencies
```cmd
pip install -r requirements.txt
```
#### Understanding Tokens
- **MASTER_TOKEN:** Acts like a license key, granting the requestor the right to send requests to Bowser.
- **PROCESS_TOKEN:** Allows the requestor to send data to and trigger processes.
- **DEVELOPER_TOKEN:** Used to change settings within Bowser, such as enabling or disabling processes.

### License
This project is licensed under the MIT License - Feel free to use it as you wish, however some credit for this project would be nice if you end up using it ;)
