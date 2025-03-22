.SILENT:

.DEFAULT: all

MPY_CROSS ?= $(shell which mpy-cross 2>/dev/null)
MPY_FLAGS ?= '-O2'

MPY_SOURCES_KMK ?= '.'

MPY_TARGET_DIR ?= compiled/

PY_TREE = $(shell find $(MPY_SOURCES) -name "*.py" -and ! -iname "boot.py" -and ! -iname "main.py")

all: clean compile

clean:
	@echo "===> Cleaning build artifacts"
	rm -rf $(MPY_TARGET_DIR)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

compile: $(PY_TREE:%.py=$(MPY_TARGET_DIR)/%.mpy)
	@echo "===> Compiling all  py files to mpy with flags $(MPY_FLAGS)"
$(MPY_TARGET_DIR)/%.mpy: %.py
	@mkdir -p $(dir $@)
	@$(MPY_CROSS) $(MPY_FLAGS) $? -o $@
