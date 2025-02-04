import os
import subprocess
import platform

class ProWorks:
    def __init__(self):
        if platform.system() != "Windows":
            raise EnvironmentError("ProWorks can only be run on Windows operating systems.")
        print("ProWorks initialized for Windows OS")

    def disable_startup_programs(self):
        """Disables unnecessary startup programs to enhance boot speed."""
        print("Disabling unnecessary startup programs...")
        subprocess.run("powershell Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run' -Name '*' -Value $null -Force", shell=True)
        print("Startup programs disabled.")

    def optimize_memory(self):
        """Adjusts virtual memory settings for optimal performance."""
        print("Optimizing virtual memory settings...")
        subprocess.run("powershell Set-ItemProperty -Path 'HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management' -Name 'PagingFiles' -Value 'C:\\pagefile.sys 4096 8192'", shell=True)
        print("Virtual memory optimized.")

    def clean_temp_files(self):
        """Cleans temporary files to free up disk space."""
        temp_dir = os.environ.get('TEMP', r'C:\\Windows\\Temp')
        print(f"Cleaning temporary files in {temp_dir}...")
        for root, dirs, files in os.walk(temp_dir):
            for name in files:
                try:
                    os.remove(os.path.join(root, name))
                except Exception as e:
                    print(f"Error removing file {name}: {e}")
        print("Temporary files cleaned.")

    def tune_network_settings(self):
        """Tunes network settings for better connectivity."""
        print("Tuning network settings for better performance...")
        subprocess.run("netsh int tcp set global autotuninglevel=normal", shell=True)
        print("Network settings tuned.")

    def run_all_tweaks(self):
        """Runs all available system tweaks."""
        print("Running all system tweaks...")
        self.disable_startup_programs()
        self.optimize_memory()
        self.clean_temp_files()
        self.tune_network_settings()
        print("All system tweaks applied successfully.")

if __name__ == "__main__":
    proworks = ProWorks()
    proworks.run_all_tweaks()