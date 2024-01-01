Shemmy Website
================================

# directory definitions

PROJECT_ROOT = Project home directory (where settings.py is)
BASE_DIR = manage.py home directory
HTDOCS_ROOT = PROJECT_ROOT  (static and media files locally)

# Running locally

### Step 1) Docker install
First install docker (which should include docker-compose). Your
preferred method is probably fine.https://docs.docker.com/get-docker/
Otherwise the following should work, this installs docker "engine"
which is just the CLI necessities.

    # uninstall old first
    for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done

    # update apt and packages to allow https repo connect
    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg

    # add docker gpg key
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
    # add apt repo
    echo \
    "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    # finally install docker toolset
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


Steps above based on https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

### Step 2) Poetry install

Poetry is our python dependency management and pacakaging tool of choice. Install as follows.

        curl -sSL https://install.python-poetry.org | python3 -


### Step 3) Copy and adjust env vars

The project will expect a `.env` file with configuration variables to
be present. Copy the example file as follows, review the defaults and
change as desired for your machine.

    cp env-example .env

    nano .env
    # OR
    vim .env


In particular look at database name/user/password and media and static
root locations.

THEORETICALLY, you will not need a .env for a production environment,
though there may be some values which do not have a default
(SECRET_KEY, etc.).  IF you do not define those values in the
production environment, the app will not run.  There is an environment
variable ENVIRONMENT defined as 'local', 'dev', or 'prod'. You may use
this variable to conditionally load or change settings based on if
it's local development, or dev/staging, or production.  DO NOT create
separate settings files.

### Step 4) Choose backing services

Review `docker-compose.yml` and remove entries under services that you
don't need.

### Step 5) Run backing services and django

To get a local copy of the server running, use docker-compose to run
the backing services (Postgresql, MailHog, Redis, etc).  Create a
virtualenv (I prefer pyenv or asdf) for the project, and install all
the packages with poetry install. Then run the main application as
usual with manage.py.

    # create virtual env HERE
    python -m venv <projectname>

    docker-compose up

    poetry install --dev --no-root


    ./manage.py migrate
    ./manage.py runserver

### Step 6) Set up pre-commit hooks

Pre-commit will run some code cleanup/formatting tools before each commit
so that your code "cleaned as you go" without extra thought.

    poetry run pre-commit install
    poetry run pre-commit run --all-files # optional

Additional pre-commit hooks can be configured in .pre-commit-config.yml
and tool specfic settings can also be found in pyproject.toml. By default
only line length is set.
