
# Mojo Timer

This project is a simple Python-based HTTP server that allows users to control a timer through various API endpoints. The server provides features such as starting, pausing, stopping, resetting, and checking the current status of the timer. Additionally, it allows setting a specific reset time after which the timer will automatically reset.

## Features
- **Start Timer**: Begin the timer from where it was paused or reset.
- **Pause Timer**: Pause the timer and save the elapsed time.
- **Stop Timer**: Stop the timer and reset the elapsed time to zero.
- **Reset Timer**: Reset the timer to 00:00:00.
- **State**: Check the current time and status (running or paused) of the timer.
- **Set Reset Time**: Set a specific time (in seconds) to automatically reset the timer.

## API Endpoints

### `/start`
Starts the timer. If the timer is already running, it will continue from where it was paused.

### `/pause`
Pauses the timer and saves the elapsed time. The timer can be resumed from this point later.

### `/stop`
Stops the timer and resets the elapsed time to 00:00:00.

### `/reset`
Resets the timer to 00:00:00 and stops the timer if it is running.

### `/state`
Returns the current time of the timer in the format `HH:MM:SS` and the status (whether the timer is running or paused).

### `/set-reset-time?time=<seconds>`
Sets a specific reset time (in seconds). The timer will automatically reset after this time has passed.

## How to Use

1. Clone or download this repository.
2. Run the Python script `main.py` to start the server.
3. Open a web browser or use an API client (e.g., Postman) to interact with the server at `http://localhost:8000`.


## Requirements

- Python 3.x or higher

## Installation

1. Clone the repository to your local machine.
   ```
   git clone https://github.com/Muhammad-Noraeii/Mojo-Timer.git
   ```
2. Navigate to the project directory.
   ```
   cd Mojo-Timer
   ```
3. Run the Python script to start the server.
   ```
   python3 main.py
   ```

4. The server will be running at `http://localhost:8000`. You can now interact with the timer using the provided API endpoints.

---
