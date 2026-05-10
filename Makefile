APP_NAME=ktools
ENTRY=main.py

PYINSTALLER=pyinstaller

# =====================================================
# CLEAN
# =====================================================

clean:
	python -c "import shutil, os, glob; \
	shutil.rmtree('build', ignore_errors=True); \
	shutil.rmtree('dist', ignore_errors=True); \
	[os.remove(f) for f in glob.glob('*.spec')]"

# =====================================================
# BUILD (macOS .app)
# =====================================================

build:
	$(PYINSTALLER) \
		--clean \
		--windowed \
		--name $(APP_NAME) \
		--collect-all matplotlib \
		--add-data "app/views/styles/themes:app/views/styles/themes" \
		--add-data "app/resources:app/resources" \
		$(ENTRY)

# =====================================================
# DEBUG BUILD (console açık)
# =====================================================

debug:
	$(PYINSTALLER) \
		--clean \
		--windowed \
		--console \
		--name $(APP_NAME)_debug \
		--collect-all matplotlib \
		--add-data "app/views/styles/themes:app/views/styles/themes" \
		--add-data "resources:resources" \
		$(ENTRY)

# =====================================================
# RUN (source code)
# =====================================================

run:
	python $(ENTRY)