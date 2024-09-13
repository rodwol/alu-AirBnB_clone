# AirBnB Clone

## Overview

This project is an AirBnB clone, developed to understand the core functionalities of an object-oriented application. It involves creating a command-line interpreter to manage various AirBnB objects such as Users, States, Cities, Places, and more. The project includes tasks like defining a base model, implementing serialization/deserialization methods, and building a file storage engine.

## Features

- **Command Interpreter:** Manage AirBnB objects through a command-line interface.
- **Base Model:** Provides a base class for all other classes in the project.
- **Serialization/Deserialization:** Save and load instances to/from a JSON file.
- **File Storage Engine:** Manage the storage of objects and their data.

## Installation

1. Clone this repository:

    \`\`\`
    git clone https://github.com/rodwol/alu-AirBnB_clone.git
    cd alu-AirBnB_clone
    \`\`\`

## Usage

### Command Interpreter

To start the command interpreter:

\`\`\`
python console.py
\`\`\`

### Available Commands

- **Create an object:**

    \`\`\`
    create <class_name> <arguments>
    \`\`\`

- **Show all objects:**

    \`\`\`
    all <class_name>
    \`\`\`

- **Show a specific object by ID:**

    \`\`\`
    show <class_name> <id>
    \`\`\`

- **Destroy an object by ID:**

    \`\`\`
    destroy <class_name> <id>
    \`\`\`

- **Update an object's attributes:**

    \`\`\`
    update <class_name> <id> <attribute> <value>
    \`\`\`

## File Structure

- \`models/\`: Contains all the model classes for the AirBnB objects.
- \`models/engine/\`: Contains the file storage engine and related classes.
- \`console.py\`: Command-line interpreter for managing AirBnB objects.
- \`tests/\`: Contains unittests for the project.

## Development

### Running Tests

To run the unittests:

\`\`\`
python -m unittest discover -s tests
\`\`\`

## Authors

- **Rodas Woldemichel Goniche**
- **Angelo Shema**

Contributions are welcome! Please open an issue or submit a pull request.
