import subprocess

class LinkStatus:

    def __init__(self) -> None:
        self.tcl_location = "python"

    def run_tcl(self):
        cmd = f"{self.tcl_location} test_script.py"
        subprocess.run(cmd, shell=True, check=True)
        
    