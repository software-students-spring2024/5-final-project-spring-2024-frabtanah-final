![Lint-free](https://github.com/nyu-software-engineering/containerized-app-exercise/actions/workflows/lint.yml/badge.svg)

# Final Project

## Machine Learning Plant Recognition

Our web app allows users to capture or upload an image of a plant and we will identify the name of that plant using a machine learning model. 


## Team Members

- Francisco Cunningham - [fctico11](https://github.com/fctico11)
- Ahmad Almesned - [ahmadhcs](https://github.com/ahmadhcs)
- Tanuj Sistla - [tanuj123-cyber](https://github.com/tanuj123-cyber)
- Abhi Vachani - [avachani](https://github.com/avachani)

## To run our project, locally use

```docker-compose up --build --force-recreate``` to build and run.
Then navigate to http://0.0.0.0:8000 to see the front end of the web app running and interact with our app.


### Unit Tests

To run unit tests, navigate to the root directory and use the command: ```pytest web-app/tests/test_app.py```
To check code coverage for the web-app, in the root directory run: ```pytest --cov=web-app web-app/tests```

## Link To Containers 
[Both Containers](https://hub.docker.com/r/avachani/plant-recog/tags) 

## Deployed Version
here
