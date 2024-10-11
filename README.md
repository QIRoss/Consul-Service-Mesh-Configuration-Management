# Consul Service Mesh Configuration Management

Studies based in day 29-30 of 100 Days System Design for DevOps and Cloud Engineers.

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 21–30: Advanced Infrastructure as Code (IaC)

Day 29–30: Study and implement cloud-native configuration management using Consul.

## Project Overview

Each initial folder is an alternative project to Consul basics in dev mode (without mTLS and credentials):

```consul-fastapi```: this starting project teaches how to browse to ```localhost:8500``` and build you own configuration key to get the configuration values into a FastAPI application.

```consul-service-discovery```: this project shows basics of service discovery.

```consul-service-discovery-scalling```: this project extends scalling to load balancing replicas in a service mesh.

## ```consul-fastapi```

```
docker-compose up --build
```
Browse to ```localhost:8500``` create a key with name ```config/myapp``` and a value you want.
```
curl http://localhost:8000/config
```
This shows how your starting application got basic configurations from Consul.

## ```consul-service-discovery```

This service is based in service discovering a service A to a service B get the message from an API endpoint.
Consul is responsible for register services so they can be consulted by another services.

```
docker-compose up --build
curl http://localhost:8001/greet
curl http://localhost:8002/get-greeting
```

You will see the same message in different application thanks to Consul service discovery register.

## ```consul-service-discovery-scalling```

```
docker-compose up --build --scale service_a=3
```
This way you will see multiple service_a.
```
curl http://http://localhost:8002/get-greeting
```
Open a terminal side by side to check in docker-compose logs which service_a replica is responsible by the answer in service_b.
You can see it still working after deleting a single instance.
```
docker stop consul-service-discovery-scaling-service_a-1
curl http://http://localhost:8002/get-greeting
```
Keep checking docker-compose logs to see the remaining replicas answering.

## Author
This project was implemented by [Lucas de Queiroz dos Reis][2]. It is based on the Day 23–24: Automate multi-environment setups using Terraform and Ansible dynamic inventories from the [100 Days System Design for DevOps and Cloud Engineers][1].

[1]: https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f "Medium - Deo Shankar 100 Days"
[2]: https://www.linkedin.com/in/lucas-de-queiroz/ "LinkedIn - Lucas de Queiroz"