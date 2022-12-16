# DevOps
Repository for the devops lecture of the fifth semester

# Responsables
- Benjamin Bilal Bhatti
- Linus Baumann
- Jonas Haberstroh

# honarary members
- Lasse Henrich
- Thomas Alpert

# Dockerized the Application
The source code of the web app is available under [app->app](./app/app/). <br>
The dockerfile creating the container for the web app is under [app->dockerfile](./app/dockerfile). <br>
The docker-compose file is located under [docker-compose.yaml](./docker-compose.yaml).

# Testing
- The sonarqube can be locally used with following docker command:
  - docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest
- For the continuous integration pipeline the setup proccess is as follows:
  1. Startup the Azure-VM (Contact: Linus Baumann)
  2. Refresh the github secret "SONAR_HOST_URL" because the IP address of the VM will change, each time it is started.
  3. Now the pipeline can be run.
  4. Don't forget to shut down the Azure-VM after it is not needed, as keeping it running will continually cost money.

# Delivery
- The delivery can be started by manually activating the cd pipeline.
- What this pipeline does, is pushing the project to Docker Hub and publish as a Azure WebApp.
- For the new version to be accessible online, the WebApp will then only have to be started.