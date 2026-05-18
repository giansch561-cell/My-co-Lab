# My-co-Lab
# Camera Module Draft V0

from datetime import datetime

def capture_image():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{timestamp}] Capture image")

if __name__ == "__main__":
    capture_image()