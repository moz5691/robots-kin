# Robots Kinematics


## Usage

### Enable Google OAuth2, and use your Google ClientId and ClientSecret.  
Update provided ```.env.example``` and rename it to ```.env```.  ```docker-compose.yml``` uses environmental variables in ```.env``` file.

```
# .env 
GOOGLE_CLIENT_ID=bring-your-own
GOOGLE_CLIENT_SECRET=bring-your-own
```

### Run dev environment
```shell
docker-compose up -d --build
```

### Run postgres client
```shell
docker-compose exec robots-db psql -U postgres
```

### Run pytest
```shell
docker-compose exec api python -m pytest 
```

### Use Swagger with browser
Browse with the following url and click on ```OpenAPI```
```shell
http://localhost:8004
```
![nav_bar](img/nav_bar.png)

The following is screenshot of OpenAPI
![openapi](img/openapi.png)

Robot tracker is one of feature.  You can track a robot_id and its average location data.
![tracker](img/tracker.png)


## Todos

- [ ] Protect private routes
- [ ] Pytest
- [ ] K8s set up
- [ ] Create Helm Chart

## Troubleshoot

I have struggled to get Poetry working on Python 3.10.x. I think the reason was I have installed Poetry with Python 3.9.x and upgraded to 3.10.x

Run the following in Python virtual environment if you run into a trouble to run ```poetry```.
```shell
pip install cleo tomlkit poetry.core requests cachecontrol cachy html5lib pkginfo virtualenv lockfile
```