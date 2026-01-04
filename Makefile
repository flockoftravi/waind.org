.PHONY: html clean serve publish

html:
	uv run pelican content -s pelicanconf.py

clean:
	rm -rf output

serve:
	uv run pelican --listen --autoreload

publish:
	uv run pelican content -s publishconf.py
