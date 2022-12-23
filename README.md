# minisearch

A simple search form using django framework

![](/images/index.png)
![](/images/results.png)
![](/images/empty-state.png)


## Installation

To install this app locally you can use on of the following..

### Docker image
#### Dependencies
- [Docker](https://docs.docker.com/engine/install/)

#### Build `Dockerfile` locally

In order to build a local image you need to clone this repository using this command
```bash
git clone https://github.com/mostafa-yasen/minisearch.git
```

Then enter the project directory `cd minisearch`. Now you can build the `Dockerfile` using the command

```bash
docker build . -t minisearch:1.0
```

After a successfull build you can now run the image using
```bash
docker run -d -p 80:8000 minisearch:1.0
```

Now you can find the web app running on you local machine. To access it, open your browser and write `localhost` or `127.0.0.1` in the address bar and hit enter.

### Python environment
#### Dependencies
- [Python 3.6+](https://www.python.org/downloads/)

You can clone the project using
```bash
git clone https://github.com/mostafa-yasen/minisearch.git
```

Then enter the project directory `cd minisearch`.

First of all you need to setup a virtual environment. Create one using this command
```sh
python3 -m venv venv
```

if you don't already have virtualenv module installed, install it using this command `pip install virtualenv`. After creating it, run the following command to activate it
```sh
source ./venv/bin/activate
```

Next step is to install requirements from the `requirements.txt` file. Install them using this command

```sh
pip install -r requirements.txt
```
After you successfully install requiremetns, you can now run the project using this command

```sh
python minisearch/manage.py runserver 8000
```

You should now see the index page on your browser at `localhost:8000`.
