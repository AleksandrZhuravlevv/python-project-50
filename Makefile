install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-install-force:
	python3 -m pip install --user --force-reinstall dist/*.whl

coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest




