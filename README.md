# Optimo Development recruitment task

  

The program aims to generate the numbers of the Fibonacci sequence.

It consists of 3 services cooperating each other:

-  **Generator** is responsible for generating Fibonacci numbers with a predefined delay and pushing these onto RabbitMQ queue;

-  **Ingest** is responsible for the consumption of numbers and storage them in the MySQL database;

-  **Api** - RestAPI - is responsible for returning numbers of the Fibonacci sequence.

  

All of the services and database are configured and linked via the docker-compose tool.

  

## How to use

At first, the user should build services using the command:

`$ docker-compose build`

To start services the user should use the following command:

`$ docker-compose up`

Usage of this command results starting services: at first RabbitMQ server and MySQL database, then services Generator, Ingest and Api. The first usage can take some time because docker has to pull images of services and set up an all-important configuration.

It is possible to crush the creation of some services. In such a case, the user should either wait for the restart of services or use CTRL+C to stop services and start them again.

The Fibonacci numbers are generated and returned on [http://localhost:5000/](http://localhost:5000/).

  

## Further development

1. Storage credentials not as a plain text in docker-compose.

3. Usage of asyncio.

4. Usage of Unittests.