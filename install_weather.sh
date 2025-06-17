#!/data/data/com.termux/files/usr/bin/bash

INSTALL_DIR="$HOME/.weather"
SCRIPT_NAME="weather_cli_ui.py"
ALIAS_NAME="weather"
BASHRC="$HOME/.bashrc"

mkdir -p "$INSTALL_DIR"
cp "$SCRIPT_NAME" "$INSTALL_DIR/"

if ! grep -q "$ALIAS_NAME=" "$BASHRC"; then
  echo "alias $ALIAS_NAME='python $INSTALL_DIR/$SCRIPT_NAME'" >> "$BASHRC"
  echo "✅ Alias added to .bashrc"
fi

source "$BASHRC"

echo -e "\n🎉 Weather tool installed successfully!"
echo "👉 Ab bas likho: weather"
