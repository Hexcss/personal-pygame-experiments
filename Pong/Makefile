# Makefile for Pygame Project

# Variables
VENV_DIR := venv
SRC_DIR := src
REQ_FILE := requirements.txt
START_SCRIPT := run.sh

.PHONY: all create run install clean enter vs

# Default task
all: run

# Create project structure, virtual environment, and necessary files
create:
	@echo "Creating project structure..."
	@mkdir -p $(SRC_DIR)
	@python3 -m venv $(VENV_DIR)
	@touch $(REQ_FILE)
	@echo "#!/bin/bash\nsource $(VENV_DIR)/bin/activate\npython3 $(SRC_DIR)/main.py" > $(START_SCRIPT)
	@chmod +x $(START_SCRIPT)
	@touch $(SRC_DIR)/main.py
	@echo "import pygame\n\ndef main():\n    pygame.init()\n    screen = pygame.display.set_mode((800, 600))\n    pygame.display.set_caption('Pygame Project')\n    running = True\n    while running:\n        for event in pygame.event.get():\n            if event.type == pygame.QUIT:\n                running = False\n        screen.fill((0, 0, 0))\n        pygame.display.flip()\n    pygame.quit()\n\nif __name__ == '__main__':\n    main()" > $(SRC_DIR)/main.py
	@echo '{\n  "venvPath": "./",\n  "venv": "$(VENV_DIR)",\n  "pythonVersion": "3.x"  // Replace with your Python version\n}' > pyrightconfig.json
	@echo "Project structure created successfully, including pyrightconfig.json."

# Run the project using the start script
run:
	@echo "Running the project..."
	@./$(START_SCRIPT)

# Install dependencies inside the virtual environment and update requirements.txt
install:
	@echo "Installing dependency..."
	@$(VENV_DIR)/bin/pip install $(package)
	@$(VENV_DIR)/bin/pip freeze | grep $(package) >> $(REQ_FILE)
	@echo "Dependency installed and added to $(REQ_FILE)."

# Enter the source directory
enter:
	@echo "Navigating to the source directory..."
	@cd $(SRC_DIR) && exec $$SHELL

# Enter the virtual environment shell
vs:
	@echo "Entering virtual environment shell..."
	@$(VENV_DIR)/bin/activate.fish; exec fish

# Clean the project by removing the virtual environment and all generated files
clean:
	@echo "Cleaning project..."
	@rm -rf $(VENV_DIR)
	@rm -rf $(SRC_DIR)
	@rm -f $(REQ_FILE)
	@rm -f $(START_SCRIPT)
	@echo "Project cleaned."

# Usage instruction
help:
	@echo "Available commands:"
	@echo "  make create           - Create project structure with src, venv, and initial files."
	@echo "  make run              - Run the project using the start script."
	@echo "  make install package=<package_name> - Install a package inside the venv and add it to requirements.txt."
	@echo "  make enter            - Navigate to the source directory."
	@echo "  make vs               - Enter the virtual environment shell."
	@echo "  make clean            - Clean the project by removing venv, src, and all generated files."
	@echo "  make help             - Display this help message."
