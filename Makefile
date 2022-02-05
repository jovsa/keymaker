environment:
	if ! [[ -d ".venv/bin/" ]]; then python -m venv .venv; fi
	echo "Installing required python packages."; \
	source .venv/bin/activate; \
	pip install -r requirements.txt; \
	echo "Finished installing required python packages, deactivating environment"; \
	deactivate
