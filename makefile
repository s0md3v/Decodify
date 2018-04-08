install:
	@sudo cp dcode /usr/local/bin/
	@sudo chmod +x /usr/local/bin/dcode
	@echo "Everything is setup! Enter 'dcode <string>' in terminal to use decodify"

uninstall:
	@sudo rm -f /usr/local/bin/dcode
	@echo "Decode has been removed"
