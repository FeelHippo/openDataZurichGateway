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

### Layout
https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/

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

### Docs
http://127.0.0.1:8080/apidocs/

### Test application
python -m pytest

<p align="right">(<a href="#readme-top">back to top</a>)</p>
