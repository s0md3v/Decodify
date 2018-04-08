DESTDIR ?= /usr/local/bin

install:
	@sudo cp dcode $(DESTDIR)
	@sudo chmod +x $(DESTDIR)/dcode
	@echo "Everything is setup! Enter 'dcode <string>' in terminal to use decodify"

uninstall:
	@sudo rm -f $(DESTDIR)/dcode
	@echo "Decodify has been removed"
