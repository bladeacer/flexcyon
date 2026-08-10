.PHONY: help migrate test run release

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  test         Runs unit tests, generates test.json"
	@echo "  run          Runs testing then migration script"
	@echo "  watch        Watches for file changes and runs 'make run' automatically"
	@echo "  release      Release new version with helper shell script."

test:
	./scripts/migration/test_migrator.py scripts/migration/test.json

run:
	$(MAKE) test
	./scripts/migration/migrator.py scripts/migration/test.json

watch:
	./scripts/fs.py

release:
	@./scripts/version.sh
