from ._imports import *
import subprocess


def wsl_show(fig, file_path): 
    fig.savefig(file_path, dpi=300, bbox_inches='tight')
    os.system(f"powershell.exe start {file_path}")

def wsl_open(file_path): 
    os.system(f"powershell.exe start {file_path}")
