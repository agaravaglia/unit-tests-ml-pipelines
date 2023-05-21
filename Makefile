clean_pycache:
	@sh bash/clean_pycache.sh

run_pytest:
	@sh bash/run_pytest.sh $(path)

pytest: run_pytest clean_pycache

pipeline:
	sh bash/run_pipeline.sh $(step)