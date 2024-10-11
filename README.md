# Consul Service Mesh Configuration Management

Studies based in day 29-30 of 100 Days System Design for DevOps and Cloud Engineers.

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 21–30: Advanced Infrastructure as Code (IaC)

Day 29–30: Study and implement cloud-native configuration management using Consul.

## Project Overview

Each initial folder is an alternative project from my studies:

```consul-fastapi```: this starting project teaches how to browse to ```localhost:8500``` and build you own configuration key to get the configuration values into a FastAPI application.


## ```consul-fastapi```

```
docker-compose up --build
```
Browse to ```localhost:8500``` create a key with name ```config/myapp``` and a value you want.
```
curl http://localhost:8000/config
```
This shows how your starting application got basic configurations from Consul.

## Author
This project was implemented by [Lucas de Queiroz dos Reis][2]. It is based on the Day 23–24: Automate multi-environment setups using Terraform and Ansible dynamic inventories from the [100 Days System Design for DevOps and Cloud Engineers][1].

[1]: https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f "Medium - Deo Shankar 100 Days"
[2]: https://www.linkedin.com/in/lucas-de-queiroz/ "LinkedIn - Lucas de Queiroz"