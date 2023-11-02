# bf-docker-image

## Setup:

1- Before proceeding, ensure you've installed Docker by referring to the installation guide available at the following link: [Docker Installation Guide](https://docs.docker.com/engine/install/).

2- Build the deal.II image by executing the subsequent terminal command:

````
docker pull dealii/dealii:v9.4.0-focal
````

3- Go to the project directory and open the terminal there.

4- Create the project image by running the following command in the terminal:

````
docker build -t bf-docker .
````

5- Run the Docker Image by running the following command in the terminal:

````
docker run -it bf-docker:latest
````







  
