install:
	@echo "Installing Totem..."
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
