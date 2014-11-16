NAME="The Great Escape"
GAME=TheGreatEscape
BUILD?=build
OPTIONS=-H

.PHONY: usage
usage:
	@echo "Supported targets:"
	@echo "  usage		Show this help"
	@echo "  install	Install the $(NAME) support script"
	@echo "  skool		Build the $(NAME) skool file"
	@echo "  disasm	Build the $(NAME) disassembly"
	@echo "  asm		Build the $(NAME) assembly"
	@echo "  bin		Build the $(NAME) binary image"
	@echo "  tap		Build the $(NAME) tape image"
	@echo "  clean		Clean a previous build"
	@echo ""
	@echo "Environment variables:"
	@echo "  BUILD          directory in which to build the disassemblies (default: build)"

.PHONY: install
install:
	mkdir -p ~/.skoolkit
	cp $(GAME).py ~/.skoolkit

.PHONY: skool
skool:
	mkdir -p $(BUILD)
	sna2skool.py $(OPTIONS) -R -c $(GAME).ctl $(GAME).z80 > $(BUILD)/$(GAME).skool 

.PHONY: disasm
disasm: skool
	skool2html.py $(OPTIONS) -o $(BUILD)/$(GAME).skool

.PHONY: asm
asm: skool
	skool2asm.py -H -c $(BUILD)/$(GAME).skool > $(BUILD)/$(GAME).asm

.PHONY: bin
bin: asm
	pasmo -v --bin $(BUILD)/$(GAME).asm $(BUILD)/$(GAME).bin

.PHONY: tap
tap: bin
	bin2tap.py --org 16384 --stack 65535 --start 61795 $(BUILD)/$(GAME).bin

.PHONY: clean
clean:
	@echo 'Cleaning...'
	-rm -rf $(BUILD)

