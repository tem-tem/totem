#!/bin/bash
echo "Installing Totem..."
curl -L -o totem https://raw.githubusercontent.com/tem-tem/totem/main/totem
chmod +x totem
sudo mv totem /usr/local/bin/
echo "Totem installed! Run 'totem t 12:30' to test."
echo "Run 'totem c \"2 + 3 * (2 + 22)/2\"' to test."
