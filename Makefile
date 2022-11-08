build:
	python -m pip install --upgrade pip
	pip install --user poetry
	poetry install

format_everything:
	pre-commit run --all-files

update:
	poetry update

test:
	.venv/bin/pytest

clean:
	find ./ -type d -name ".pytest_cache" | xargs rm -rf
	find ./ -type d -name "__pycache__" | xargs rm -rf
	find ./ -type d -name ".benchmarks" | xargs rm -rf
	find ./ -type d -name "dist" | xargs rm -rf
