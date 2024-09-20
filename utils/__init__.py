import sys
from pathlib import Path

# Get the base directory of the project
BASE_DIR = Path(__file__).resolve().parents[2]

# Add the base directory to the system path
sys.path.append(str(BASE_DIR))
