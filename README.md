# Pattern to set up python iohttp server which is wrapped in gunicorn and is dockerized via Docker

This project demonstrate:
- how to deploy several instances of iohttp server in Docker containers with Gunicorn;
- deploy nginx instance in Docker container;
- proxy the load through nginx with upstreams into iohttp instances.

## Deployment
To get up the infrastructure you should:
```shell script
make up
```

To turn off the infrastructure you should:
```shell script
make down
```