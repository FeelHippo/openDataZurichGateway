<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#layout">Layout</a></li>
        <li><a href="#run-application">Run application</a></li>
        <li><a href="#api-docs">API Swagger Docs</a></li>
        <li><a href="#test">Test</a></li>
      </ul>
    </li>
    <li>
      <a href="#deployment">Deployment</a>
      <ul>
        <li><a href="#aws-ec2">AWS EC2 Ubuntu Server</a></li>
        <li><a href="#ci-cd">CI/CD</a></li>
        <li><a href="#s3">Cloud Object Storage</a></li>
        <li><a href="#cdn">Content Delivery Network (CDN)</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

* A microservice API to proxy data from Zurich's [Geoportal](https://opendatazurich.github.io/geoportal/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- BUILT WITH -->
### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/3.0.x/#)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

<!-- LAYOUT -->
### Layout
https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/

<!-- RUN APPLICATION -->
### Run application
- Activate the virtual environment
`.venv\Scripts\activate`
- Within the virtual environment, install Flask
`pip install Flask`
- install env files
`pip install python-dotenv`
- install missing modules
`pip install <name of missing module here>`
- Run App
`flask --app flaskr/__init__.py run`

<!-- API DOCS -->
### Docs
http://127.0.0.1:8080/apidocs/

<!-- TEST -->
### Test application // WIP
python -m pytest

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DEPLOYMENT -->
## Deployment

<!-- AWS EC2 -->
### AWS EC2
This microservice is deployed on [this](https://eu-north-1.console.aws.amazon.com/ec2/home?region=eu-north-1#InstanceDetails:instanceId=i-0e020cb9184f8d174) EC2 instance.
It is accessible from a [Public IPv4 DNS](ec2-16-170-122-157.eu-north-1.compute.amazonaws.com) for now might change in the near future. 
Some useful resources:
- [Deploying to a server via SSH and Rsync in a Github Action](https://zellwk.com/blog/github-actions-deploy/)
- [Connect to your Linux instance using an SSH client](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html). In my case, assuming the ssh client/bash is running along with the .pem certificate: ssh -i stadtplan-mobile-app-key-pair.pem ubuntu@ec2-16-170-122-157.eu-north-1.compute.amazonaws.com.
- [AWS default usernames](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html)
- [Deploy your Node App to EC2 with Github Actions](https://medium.com/@ikbenezer/deploy-your-node-app-to-ec2-with-github-actions-364df98d9918)
- [Deploying Flask App With PM2 on Ubuntu Server 18.04](https://gokhang1327.medium.com/deploying-flask-app-with-pm2-on-ubuntu-server-18-04-992dfd808079)
- [create venv without sudo to be able to work (esp. write) in it without sudo](https://stackoverflow.com/a/19472082). This is taken care of by the [github workflow](https://github.com/FeelHippo/openDataZurichGateway/blob/main/.github/workflows/deploy.yml)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CI CD -->
[See github workflow for details](https://github.com/FeelHippo/openDataZurichGateway/blob/main/.github/workflows/deploy.yml)

<!-- S3 -->
[App assets are stored in an S3 bucket](https://eu-north-1.console.aws.amazon.com/s3/buckets/stadtplan-mobile-app?region=eu-north-1&bucketType=general&tab=objects)

<!-- CDN -->
[Cached copy of files from S3 are served to the app through Cloud Front](https://us-east-1.console.aws.amazon.com/cloudfront/v4/home?region=eu-north-1#/distributions/E346HDBF627ISG/behaviors) 
