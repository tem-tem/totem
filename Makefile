install:
	@echo "Installing Totem..."
	@echo "Checking for Python and pip..."
	@if ! command -v python3 &>/dev/null; then echo "Python3 is not installed. Please install Python3 first."; exit 1; fi
	@if ! command -v pip3 &>/dev/null; then echo "pip3 is not installed. Installing pip3..."; sudo apt install -y python3-pip || sudo pacman -S --noconfirm python-pip || brew install python; fi
	@echo "Installing required Python packages..."
	@pip3 install --upgrade pip
	@pip3 install -r requirements.txt
	@chmod +x totem.py
	@cp totem.py totem  # Copy the script and rename it
	@sudo mv totem /usr/local/bin/
	@echo "Totem installed successfully! Run 'totem t 12:30' to test."

uninstall:
	@echo "Removing Totem..."
	@sudo rm -f /usr/local/bin/totem
	@echo "Totem removed."

test:
	@echo "Running test..."
	@./totem.py t 12:30
