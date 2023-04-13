# ADHD-API

Here you can find the API

### Docker commands

__To build the image:__

>docker build -t adhd-api .

__To run the container:__

>docker run -d --name adhd-api-container --network adhd -p 80000:8000 adhd-api

__To image (for newer image versions):__

>docker tag <your_image_name> <registry_username>/<repository_name>:<tag>

>docker tag adhd-api bajraktari/adhd-api:vx.x.x

__To push image to Dockerhub:__

>docker push <registry_username>/<repository_name>:<tag>

>docker push bajraktari/adhd-api:vx.x.x