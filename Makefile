.PHONY: help test

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  test         Runs unit tests, generates test.json"
	@echo "  run          Runs script with generated test.json"

test:
	./test_migrator.py

run:
	$(MAKE) test
	./migrator.py test.json
