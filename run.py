import os
import subprocess
import sys
import time
import logging

def setup_logging(log_dir):
    log_path = os.path.join(log_dir, "app.log")
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_path, mode='a'),
            logging.StreamHandler(sys.stdout)
        ]
    )

def main():
    # Get the current directory where the script is located
    if getattr(sys, 'frozen', False):
        current_dir = sys._MEIPASS
        base_dir = os.path.dirname(sys.executable)  # real folder
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = current_dir

    setup_logging(base_dir)

    logging.info("Starting application...")

    # Path to applyConfig.bat
    webcam_config_path = os.path.join(current_dir, "applyConfig.bat")
    logging.debug(f"Webcam config path: {webcam_config_path}")

    # Path to OBS executable (assumed constant across machines)
    obs_path = r"C:\Program Files\obs-studio\bin\64bit\obs64.exe"

    if not os.path.exists(webcam_config_path):
        logging.error("applyConfig.bat not found in script directory.")
        sys.exit(1)

    if not os.path.exists(obs_path):
        logging.error("OBS not found at expected location.")
        sys.exit(1)

    try:
        obs_dir = os.path.dirname(obs_path)
        subprocess.Popen([obs_path], cwd=obs_dir)
        logging.info("OBS launched.")
    except Exception as e:
        logging.exception(f"Failed to launch OBS: {e}")
        sys.exit(1)

    logging.info("Waiting for OBS to initialize...")
    time.sleep(8)

    try:
        subprocess.run([webcam_config_path], check=True)
        logging.info("Webcam settings applied.")
    except subprocess.CalledProcessError as e:
        logging.error("Failed to run applyConfig.bat.")
        logging.exception(e)
        sys.exit(1)

    logging.info("Process completed successfully.")

if __name__ == "__main__":
    main()
