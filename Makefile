.PHONY: help migrate test run

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  test         Runs unit tests, generates test.json"
	@echo "  run          Runs testing then migration script"

test:
	./test_migrator.py

run:
	$(MAKE) test
	./migrator.py test.json
