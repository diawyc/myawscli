# AWS HA

## Architecture Overview
![Architecture Diagram](https://static.us-east-1.prod.workshops.aws/public/5275bcf4-7b53-42b4-8eee-5d6edd6ac63f/static/images/ha-webapp/HA-LAB.svg)

In this architecture, a public-facing Application Load Balancer forwards client traffic to our web tier EC2 instances. The web tier is running Nginx webservers that are configured to serve a React.js website and redirects our API calls to the application tier’s internal facing load balancer. The internal  

## Workshop Instructions:

See [Highly Available Web App](https://catalog.us-east-1.prod.workshops.aws/workshops/5ceb632a-c07f-44a5-a3bd-b8f616a631c0/en-US/introduction/overview))

# CLI
## [Module 1](module1.md)
## [Module 2](module2.md)



