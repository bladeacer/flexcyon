.PHONY: help migrate test run

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  test         Runs unit tests, generates test.json"
	@echo "  run          Runs testing then migration script"
	@echo "  watch        Watches for file changes and runs 'make run' automatically"

test:
	./test_migrator.py

run:
	$(MAKE) test
	./migrator.py test.json

watch:
	./fs.py
