import subprocess
import sys

def init_packages() -> None:
    try:
        import prettytable
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "prettytable"])
    
    try:
        import PyQt5
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt5"])

init_packages()