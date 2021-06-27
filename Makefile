run-tests:
	@pipenv run pytest -p no:cacheprovider tests/

run-code-formatter:
	@pipenv run black .
