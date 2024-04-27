![Lint-free](https://github.com/nyu-software-engineering/containerized-app-exercise/actions/workflows/lint.yml/badge.svg)

# Final Project

## MoodMap + Machine Learning

Our app is an extension of our web app from project 2, that is, MoodMap aims to create emotional awareness through a comprehensive tracker that categorizes emotions into detailed subcategories, enabling users to monitor trends and foster personal growth on a daily and weekly basis.

However, with this app you can now take a picture and save it to your profile and run a machine learning classification model on it to tell you how you're feeling.

## Team Members

- Francisco Cunningham - [fctico11](https://github.com/fctico11)
- Ahmad Almesned - [ahmadhcs](https://github.com/ahmadhcs)
- Tanuj Sistla - [tanuj123-cyber](https://github.com/tanuj123-cyber)
- Abhi Vachani - [avachani](https://github.com/avachani)

## To run our project, use

```docker-compose up --build --force-recreate``` to build and run.
Then navigate to http://0.0.0.0:5000 to see the front end of the web app running and interact with our app.

### Unit Tests

To run unit tests, navigate to the root directory and use the command: ```pytest web-app/tests/test_app.py```

To check code coverage for the web-app, in the root directory run: ```pytest --cov=web-app web-app/tests```
