APP_NAME = ktools
ENTRY    = main.py
PYI      = pyinstaller

ADD_DATA = \
    --add-data "app/views/styles/themes:app/views/styles/themes" \
    --add-data "app/resources:app/resources"

PYI_COMMON = \
    --clean \
    --name $(APP_NAME) \
    --collect-all matplotlib \
    $(ADD_DATA)

.PHONY: run build debug clean

# =====================================================
# RUN
# =====================================================
run:
	python $(ENTRY)

# =====================================================
# BUILD (windowed)
# =====================================================
build:
	$(PYI) $(PYI_COMMON) --windowed $(ENTRY)

# =====================================================
# DEBUG BUILD (console)
# =====================================================
debug:
	$(PYI) $(PYI_COMMON) --console --name $(APP_NAME)_debug $(ENTRY)

# =====================================================
# CLEAN
# =====================================================
clean:
	rm -rf build/ dist/
	find . -type f -name "*.spec" -delete
	find . -type f -name "*.pyc"  -delete
	find . -type d -name "__pycache__"  -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "*.egg-info"    -exec rm -rf {} +
	find . -type f -name ".DS_Store" -delete
