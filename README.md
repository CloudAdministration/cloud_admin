# Cloud Administration Application

## Created with django.

---

# Running Cloud Admin using Docker Compose

This guide will walk you through the steps required to run the Cloud Admin project using Docker Compose on Linux.

## Requirements

Before you begin, make sure you have the following installed on your system:

  - Python 3.9.x
  - Virtualenv (`python3 -m pip install virtualenv`)
  - Docker
  - docker-compose


1. Clone the Repository
   - git clone https://github.com/CloudAdministration/cloud_admin.git

2. Navigate into the project directory:
   - cd cloud_admin

3. Create and activate a virtual environment:
   - python3 -m virtualenv venv
   - source venv/bin/activate

4. Install the required Python packages:
   - pip install -r requirements.txt


5. Configure the Environment
   - Create a `.env` file in the root directory of the project and add the following environment variables:
      - DEBUG=True
      - SECRET_KEY=your-secret-key
      - ALLOWED_HOSTS=127.0.0.1,localhost
      - DATABASE_URL=postgres://cloud_admin:password@db:5432/cloud_admin

Replace `your-secret-key` with a secret key of your choice.

## Build and Run the Containers

In the root directory of the project, run the following command to build and run the Docker containers:

docker-compose up --build

Once the containers are running, you can access the Cloud Admin application by navigating to `http://localhost:8000` in
your web browser.

## Stop the Containers

To stop the containers, use the following command:
-docker-compose down

## Conclusion

You now have a working instance of the Cloud Admin project running on your system using Docker Compose. If you encounter
any issues, please refer to the project documentation or the GitHub repository for further assistance.
