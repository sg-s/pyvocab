
PID := $(shell cat streamlit.pid)

.PHONY: nightly start-app stop-app restart-app install-launch-agent test coverage-report bump-version jupyter

jupyter:
	@echo "Installing kernel <pyvocab> in jupyter"
	-yes | jupyter kernelspec uninstall pyvocab
	poetry run python -m ipykernel install --user --name pyvocab




start-app: stop-app
	@echo "Starting streamlit app.."
	@bash start-app.sh

stop-app:
	@echo "Stopping streamlit app..."
	-kill $(PID)


restart-app: stop-app start-app
	@echo "Restarting app..."

test:
	poetry run coverage run -m pytest -sx --failed-first
	-rm coverage.svg
	poetry run coverage-badge -o coverage.svg

coverage-report: .coverage
	poetry run coverage html --omit="*/test*"
	open htmlcov/index.html

bump-version:
	poetry run bump