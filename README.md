# CameraCapture

Repository for handling the Camera Input

* requirements.txt -> File containing all required packages. Can be used with virtual environments
* capture.py -> Python script to open the video Capture
* picInference.py -> Python script to infer results from picture source
* vidInference.py -> Python script to infer results from video capture
* vidTrack.py -> Python script to track object that we've identified in the picture

Steps for Recreation

* Create a virtual environment with python and activate it (python -m venv .venv && .venv/Scripts/activate)
* Make sure that the python version in the virtual environment is 3.8. There are dependency issues with newer versions
* Install the packages from the requirements.txt (pip install -r requirements.txt)
* Run any of the scripts to determine the output. They can usually be found in the "runs" folder
