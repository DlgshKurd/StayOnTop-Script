# StayOnTop Script

This Python script allows you to make a specified window always on top using the `pygetwindow` and `pywin32` libraries.

## Usage

### Option 1: Run the Executable (Windows Only)

1. Go to the [Releases](https://github.com/DlgshKurd/StayOnTop-Script/releases) section of this repository.

2. Download the latest release.

3. Extract the downloaded ZIP file.

4. Run the `StayOnTop.exe` executable.

5. Switch to the window you want it to stay "always on top" and wait 3 seconds.  

6. exe closed? congrats it worked (:

### Option 2: Run the Script (Windows, macOS, Linux)

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/DlgshKurd/StayOnTop-Script.git
    ```

2. Navigate to the project directory:

    ```bash
    cd StayOnTop-Script
    ```

3. (Optional) Create and activate a virtual environment:

    ```bash
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate 
    # On macOS/Linux
    sudo apt install python3-venv
    python3 -m venv venv
    source venv/bin/activate 
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the script:

    ```bash
    # On Windows
    python StayOnTop.py
    # On macOS/Linux
    python3 StayOnTop.py
    ```
    6. Switch to the window you want it to stay "always on top" and wait 3 seconds.  

    7. Script Ended? congrats it worked (:


## Issues

If you encounter any issues or have suggestions, please [open an issue](https://github.com/DlgshKurd/StayOnTop-Script/issues).

