TGT_DIR = $(HOME)/bin

all:
	@echo Run \'make install\' to install audio-control.

install:
	@mkdir -p $(TGT_DIR)
	@cp toggle_audio.py $(TGT_DIR)/toggle-audio
	@chmod 755 $(TGT_DIR)/toggle-audio

uninstall:
	@rm $(TGT_DIR)/toggle-audio
