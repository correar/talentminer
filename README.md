# Talent Miner Project

Python web project evaluation exam

  - Responsive mobile screen
  - Form to create Tasks and Achievements
  - Table Achievement control
  - Progressive Bar achievement view
 
## Tech
    - Django 2.1
    - Python 3
    - psycopg2
    - postgreSQL

## Not Implemented
    - Edit and Delete Task and Achievements

## Installation

### Requirement
    - Docker
    - docker-compose
    
### Docker
This project is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8000, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
sudo docker-composer up --build
```
This will create the Talent Miner image and pull in the necessary dependencies. 

Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://localhost:8000
```

### If You don't have Docker

If you don't have docker installed, just download and install [Django](https://www.djangoproject.com/) and run the project

License
----

MIT


**Free Software, Hell Yeah!**