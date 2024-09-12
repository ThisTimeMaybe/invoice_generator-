import os
import subprocess

def install_dependencies():
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])

def setup_wkhtmltopdf():
    # Make sure to adjust this path to where wkhtmltopdf is installed
    os.environ['PATH'] += os.pathsep + r'C:\Program Files\wkhtmltopdf'

def main():
    install_dependencies()
    setup_wkhtmltopdf()
    print("Deployment setup is complete.")

if __name__ == "__main__":
    main()
