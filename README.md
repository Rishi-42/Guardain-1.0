# Guardian 1.0 - Web Application

Guardian 1.0 is an open-source web application designed to provide a comprehensive platform for pharmacists, counselors, and customers. This project aims to enhance access to medicines, health information, and therapy services, fostering a healthier society. Built with Django, SQLite, and modern frontend technologies, Guardian simplifies interaction between healthcare providers and users.

## Features

- **Pharmacy Hub**: Pharmacies can showcase their products, manage inventory, and receive orders seamlessly.
- **Counselor Portal**: Counselors can offer therapy sessions, set schedules, and provide mental health support online.
- **Medical Store**: Customers can research medicines, order prescriptions, and access therapy sessions conveniently.
- **Newsletter Subscription**: Customers receive weekly newsletters containing health tips and updates.
- **Responsive Design**: User-friendly interface accessible across devices, ensuring a smooth experience.
- **Google APIs Integration**: Incorporates Google APIs for calendar-based services and user authentication.
- **PayPal Payment Integration**: Secure payment gateway for seamless online transactions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rishi-42/Guardain-1.0.git
   cd Guardain-1.0


## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Rishi-42/Guardain-1.0.git
    cd Guardain-1.0
    ```

2. **Install project dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Environment Variables**: Create a `.env` file in the project root and define the necessary environment variables, including `SECRET_KEY`, `DEBUG`, `EMAIL_HOST`, `EMAIL_PASSWORD`, `GOOGLE_API_KEY`, `PAYPAL_CLIENT_ID`, etc.

4. **Run database migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Start the development server**:

    ```bash
    python manage.py runserver
    ```

6. **Access the application in your web browser at** `http://localhost:8000`

## File Structure
```
Guardian/
|-- manage.py
|-- fyp/
|   |-- fyp.py
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- asgi.py
|   |   |-- wsgi.py
|   |-- fyp/
|   |-- /pharmacy
|   |-- /counselor
|   |-- /account
|   |-- /templates
|   |-- /static
|-- .env
|-- requirements.txt
|-- README.md
|-- LICENSE
```

## Usage

### Pharmacies

1. After registering and logging in, pharmacies can:
   - Manage their products and inventory.
   - Receive and fulfill orders from customers.
   - View customer feedback and requests.
   - Upload prescription documents for customers.

### Counselors

1. After registering and logging in, counselors can:
   - Set their availability and schedule therapy sessions.
   - View customer therapy requests and respond to them.
   - Upload supporting documents and counseling materials.

### Customers

1. After registering and logging in, customers can:
   - Explore available medicines and learn about their uses and side effects.
   - Order prescriptions by uploading images or searching manually.
   - Book therapy sessions with available counselors.
   - Subscribe to weekly newsletters for health tips.



## Development Methodology

During the Production Guardian 1.0 followed the Scrum for One methodology, emphasizing iterative development, task tracking, and continuous improvement. This approach enables efficient development and ensures that the project stays aligned with its goals.

## Documentation

For detailed information about the project, please refer to the [project documentation](https://github.com/Rishi-42/Guardain-1.0/report). The documentation serves as a valuable resource for understanding how Guardian 1.0 aims, its developments and testings.

