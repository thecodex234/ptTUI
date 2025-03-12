import curses
import shutil
import os
import subprocess

print("Checking if appropriate tools installed...")

def is_command_installed(command):
    """
    Checks if a command is installed on the system.

    Args:
        command (str): The name of the command to check.

    Returns:
        bool: True if the command is installed, False otherwise.
    """
    return shutil.which(command) is not None

def install_msfconsole():
    """
    Installs the Metasploit Framework.
    """
    print("Installing Metasploit Framework...")
    try:
        os.system("""
        curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
    chmod 755 msfinstall && \
    ./msfinstall
    """)
    except:
        print("An error occurred while installing Metasploit Framework. For manual installation instructions, visit https://docs.metasploit.com/docs/using-metasploit/getting-started/nightly-installers.html")
        print("MSF Console will not be available.")
    pass

# Check if tools are installed
msfconsole_installed = is_command_installed("/opt/metasploit-framework/bin/msfconsole")
wireshark_installed = is_command_installed("wireshark")
brew_installed = is_command_installed("brew")
nmap_installed = is_command_installed("nmap")
burpsuite_installed = is_command_installed("burpsuite")
sqlmap_installed = is_command_installed("sqlmap")
aircrack_installed = is_command_installed("aircrack-ng")
hydra_installed = is_command_installed("hydra")

if not brew_installed:
    print("Brew is not installed. Is it okay to install it? y/n")
    if input() == "y":
        try:
            os.system("/bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'")
            os.system("brew install --cask wireshark-chmodbpf")
        except Exception as e:
            print(f"An error occurred while installing Brew. {e}")

if not msfconsole_installed:
    print("Metasploit Framework is not installed. Is it okay to install it? y/n")
    if input() == "y":
        install_msfconsole()

if not wireshark_installed:
    print("Wireshark is not installed. Is it okay to install it? y/n")
    if input() == "y":
        try:
            os.system("brew install --cask wireshark")
        except:
            print("An error occurred while installing Wireshark. Please install it manually.")
            print("Wireshark will not be available.")

if not nmap_installed:
    print("Nmap is not installed. Is it okay to install it? y/n")
    if input() == "y":
        try:
            os.system("brew install nmap")
        except:
            print("An error occurred while installing Nmap. Please install it manually.")
            print("Nmap will not be available.")

if not burpsuite_installed:
    print("Burp Suite is not installed. Is it okay to install it? y/n")
    if input() == "y":
        try:
            os.system("brew install --cask burp-suite")
        except:
            print("An error occurred while installing Burp Suite. Please install it manually.")
            print("Burp Suite will not be available.")

if not sqlmap_installed:
    print("SQLMap is not installed. Is it okay to install it? y/n")
    if input() == "y":
        try:
            os.system("brew install sqlmap")
        except:
            print("An error occurred while installing SQLMap. Please install it manually.")
            print("SQLMap will not be available.")

if not aircrack_installed:
    print("Aircrack-ng is not installed. Is it okay to install it? y/n")
    if input() == "y":
        try:
            os.system("brew install aircrack-ng")
        except:
            print("An error occurred while installing Aircrack-ng. Please install it manually.")
            print("Aircrack-ng will not be available.")

if not hydra_installed:
    print("Hydra is not installed. Is it okay to install it? y/n")
    if input() == "y":
        try:
            os.system("brew install hydra")
        except:
            print("An error occurred while installing Hydra. Please install it manually.")
            print("Hydra will not be available.")

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    curses.mouseinterval(0)

    # Define button positions and labels
    buttons = [
        {"label": "MSF Console", "x": 0, "y": 5, "action": "command1"},
        {"label": "Wireshark", "x": 0, "y": 6, "action": "command2"},
        {"label": "John", "x": 0, "y": 7, "action": "command3"},
        {"label": "Nmap", "x": 0, "y": 8, "action": "command4"},
        {"label": "Burp Suite", "x": 0, "y": 9, "action": "command5"},
        {"label": "SQLMap", "x": 0, "y": 10, "action": "command6"},
        {"label": "Aircrack-ng", "x": 0, "y": 11, "action": "command7"},
        {"label": "Hydra", "x": 0, "y": 12, "action": "command8"},
        {"label": "Exit", "x": 50, "y": 30, "action": "exit"},
    ]

    # Get terminal dimensions
    height, width = stdscr.getmaxyx()

    # Draw buttons
    for button in buttons:
        if button["y"] < height and button["x"] + len(button["label"]) < width:
            stdscr.addstr(button["y"], button["x"], button["label"])

    # Handle input
    while True:
        key = stdscr.getch()
        stdscr.addstr(0, 0, f"Key pressed: {key}")  # Debugging output
        stdscr.refresh()

        if key == curses.KEY_MOUSE:
            _, x, y, _, bstate = curses.getmouse()
            stdscr.addstr(1, 0, f"Mouse event: x={x}, y={y}, bstate={bstate}")  # Debugging output
            stdscr.refresh()
            if bstate & curses.BUTTON1_PRESSED:  # Left mouse button click
                for button in buttons:
                    if (
                        button["x"] <= x < button["x"] + len(button["label"])
                        and button["y"] == y
                    ):
                        stdscr.addstr(2, 0, f"Button clicked: {button['label']}")  # Debugging output
                        stdscr.refresh()
                        if button["action"] == "command1":
                            stdscr.addstr(10, 10, "Running msfconsole...")
                            stdscr.refresh()
                            subprocess.Popen(["open", "-a", "Terminal", "/opt/metasploit-framework/bin/msfconsole"]) # macOS

                        elif button["action"] == "command2":
                            stdscr.addstr(10, 10, "Running Wireshark from sudo (may require password)...")
                            stdscr.refresh()
                            subprocess.Popen(["open", "-a", "Terminal", "./Applications/Wireshark.app"]) # macOS

                        elif button["action"] == "command3":
                            stdscr.addstr(10, 10, "Running John...")
                            stdscr.refresh()
                            subprocess.Popen(["open", "-a", "Terminal", "john"])
                            # Replace with your actual command.

                        elif button["action"] == "command4":
                            stdscr.addstr(10, 10, "Running Nmap...")
                            stdscr.refresh()
                            subprocess.Popen(["open", "-a", "Terminal", "nmap"])

                        elif button["action"] == "command5":
                            stdscr.addstr(10, 10, "Running Burp Suite...")
                            stdscr.refresh()
                            subprocess.Popen(["open", "-a", "Terminal", "burpsuite"])

                        elif button["action"] == "command6":
                            stdscr.addstr(10, 10, "Running SQLMap...")
                            stdscr.refresh()
                            subprocess.Popen(["open", "-a", "Terminal", "sqlmap"])

                        elif button["action"] == "command7":
                            stdscr.addstr(10, 10, "Running Aircrack-ng...")
                            stdscr.refresh()
                            subprocess.Popen(["open", "-a", "Terminal", "aircrack-ng"])

                        elif button["action"] == "command8":
                            stdscr.addstr(10, 10, "Running Hydra...")
                            stdscr.refresh()
                            subprocess.Popen(["open", "-a", "Terminal", "hydra"])

                        elif button["action"] == "exit":
                            return

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
