from pathlib import Path
import subprocess
from os import getcwd
from os.path import join

from pathlib import Path


if __name__ == '__main__':
    BASE_DIR = Path(__file__).resolve().parents[3]
    export_command = [
        "export", f"PYTHONPATH=$PYTHONPATH:{BASE_DIR}"
    ]
    subprocess.run(export_command, shell=True)

    FILE_PATH = join(getcwd(), 'apps/platform/src/service.py')
    command = [
        "streamlit", "run", "--server.port", '8888', FILE_PATH
    ]
    subprocess.run(command)
    
