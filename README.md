# DevOps
Repository for the devops lecture of the fifth semester

# Responsables
- Benjamin Bilal Bhatti
- Linus Baumann
- Jonas Haberstroh

# honarary members
- [Lasse Henrich](@derlassehenrich)
- [Thomas Alpert](@tomisboy)

# Dockerized the Application
The source code of the web app is available under [app->app](./app/app/). <br>
The dockerfile creating the container for the web app is under [app->dockerfile](./app/dockerfile). <br>
The docker-compose file is located under [docker-compose.yaml](./docker-compose.yaml).

# Testing
The sonarqube can be used with following docker command:
- docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest