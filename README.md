# Calculus API

## Description
A FastAPI service using SymPy to perform various single and multivariable calculus operations.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Contributing](#contributing)
4. [License](#license)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/jthom2/calculus-api.git
    cd calculus-api
    ```

2. **Install Poetry** (if you don’t have it installed already):

    ```bash
    # Using pipx
    pipx install poetry

    # Or using pip
    pip install poetry
    ```

3. **Install dependencies**:

    ```bash
    poetry install
    ```

    This will install all the dependencies listed in `poetry.lock` to ensure a consistent environment.

4. **Activate the virtual environment** (optional):

    ```bash
    poetry shell
    ```

## Usage

1. **Run uvicorn**:

    ```bash
    uvicorn main:app --reload
    ```

2. **Navigate to http://127.0.0.1:8000/docs**

## Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**:

    Click the "Fork" button on the top right of the repository page.

2. **Clone your fork**:

    ```bash
    git clone https://github.com/your-username/calculus-api.git
    cd calculus-api
    ```

3. **Create a new branch**:

    ```bash
    git checkout -b feature-branch-name
    ```

4. **Make your changes**:

    Implement your feature or bug fix.

5. **Commit your changes**:

    ```bash
    git add .
    git commit -m "Description of your changes"
    ```

6. **Push to your fork**:

    ```bash
    git push origin feature-branch-name
    ```

7. **Create a pull request**:

    Go to the original repository and click the "New Pull Request" button.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.