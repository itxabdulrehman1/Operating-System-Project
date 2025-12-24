import os

def setup_logging(log_dir):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    print(f"Logs will be saved in: {log_dir}")
