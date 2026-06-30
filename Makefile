.PHONY: help migrate test run

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  test         Runs unit tests, generates test.json"
	@echo "  run          Runs testing then migration script"
	@echo "  watch        Watches for file changes and runs 'make run' automatically"

test:
	./scripts/migration/test_migrator.py scripts/migration/test.json

run:
	$(MAKE) test
	./scripts/migration/migrator.py scripts/migration/test.json

watch:
	./scripts/fs.py
