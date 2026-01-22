# Smart Surveillance System

This is a Python-based smart surveillance system that uses computer vision to detect humans and motion in video feeds.

## Features

- **Human Detection**: Uses pre-trained models to detect humans in video frames.
- **Motion Detection**: Identifies movement in the video.
- **Alert System**: Triggers alerts when detection occurs.
- **Video Capture**: Captures and processes video input.
- **Logging**: Logs events and detections.

## Installation

1. Ensure Python 3.x is installed.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python src/main.py` or use `run.bat`

## Usage

- Place input videos in `data/input_videos/`
- Detected images will be saved in `data/detected_images/`
- Check `surveillance.log` for logs.

## Project Structure

- `src/`: Source code files
- `data/`: Data directories for inputs and outputs
- `models/`: Pre-trained models
- `requirements.txt`: Python dependencies
- `run.bat`: Batch file to run the system

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Other dependencies as listed in requirements.txt

## Troubleshooting

- Ensure all dependencies are installed.
- Check that video files are in the correct format.
- Verify model files are present in `models/`