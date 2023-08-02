# AWS HA

## Architecture Overview
![Architecture Diagram](https://static.us-east-1.prod.workshops.aws/public/5275bcf4-7b53-42b4-8eee-5d6edd6ac63f/static/images/ha-webapp/HA-LAB.svg)

In this architecture, a public-facing Application Load Balancer forwards client traffic to our web tier EC2 instances. The web tier is running Nginx webservers that are configured to serve a React.js website and redirects our API calls to the application tier’s internal facing load balancer. The internal  

## Workshop Instructions:

See [Highly Available Web App](https://catalog.us-east-1.prod.workshops.aws/workshops/5ceb632a-c07f-44a5-a3bd-b8f616a631c0/en-US/introduction/overview))

# CLI
## [Part 0](part0.md)
## [Part 1](part1.md)
## [Part 2](part2.md)
## [Part 3](part3.md)
## [Part 4](part4.md)
## [Part 5](part5.md)
## [Part 6](part6.md)
## [Additional Security](part7.md)


