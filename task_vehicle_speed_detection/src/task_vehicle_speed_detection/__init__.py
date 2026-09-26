from task_vehicle_speed_detection.main import SpeedDetector
from pathlib import Path

def main() -> None:
    print("Hello from task-vehicle-speed-detection!")

    BASE_DIR = Path(__file__).resolve().parent
    RELEASES_DIR = BASE_DIR.parent / 'releases'

    model_path = str(RELEASES_DIR / 'best.pt')
    video_path = str(RELEASES_DIR / 'Task_video.mp4')

    car_radar = SpeedDetector(model_path, video_path)
    car_radar.run()