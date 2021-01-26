build:
	mkdir -pv dist && python -m zipapp -p "/usr/bin/env python" -o dist/packaged-script.pyz src/.
