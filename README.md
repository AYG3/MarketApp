# Market App
A simple Django project for an online marketplace

## Overview
This Django project provides a basic online marketplace platform, allowing users to:
- **Sign Up and Login**: Create user accounts to access the platform.
- **Browse Products**: View a list of available products.
- **Add to Cart**: Select products and add them to their shopping cart.
- **Request Products**: Submit requests to sellers for the desired products.

## Features
- **User Authentication**: Secure user authentication and authorization.
- **Product Listing**: Display a list of products with details.
- **Shopping Cart**: Allow users to add and remove products from their cart.
- **Product Requests**: Enable users to submit product requests to sellers.

## Getting Started

### Prerequisites
- **Python**: Ensure you have Python 3.x installed.
- **Virtual Environment**: Use a virtual environment to manage project dependencies.
- **Django**: Install Django using `pip install django`.

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/AYG3/MarketApp
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd marketplace
    ```

3. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment**:
    - **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    - **Linux/macOS**:
        ```bash
        source venv/bin/activate
        ```

5. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

7. **Start the Development Server**:
    ```bash
    python manage.py runserver
    ```

## Usage
1. **Access the Application**: Open your web browser and go to `http://127.0.0.1:8000/`.
2. **Sign Up**: Create a new user account.
3. **Login**: Log in to your account.
4. **Browse Products**: View the available products.
5. **Add to Cart**: Add products to your cart.
6. **Request Products**: Submit requests for products in your cart.

## Contributing
Feel free to contribute to this project by:
- **Reporting Issues**: Use the GitHub issue tracker to report bugs or suggest improvements.
- **Submitting Pull Requests**: Fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.
