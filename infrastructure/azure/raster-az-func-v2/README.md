# Deployment of raster as azure function

## Setup
* Create an azure function through the portal

* Create a python virtual environment and install the requirements
    ```bash
    python3.10 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

## Run locally
* Run the function locally
    ```bash
    func start
    ```

## Deploy
There are two options to deploy the function to azure. One can with or without publishing the local function settings and environment variables.

### Deploy without publishing local function settings
* Deploy the function to azure and add the function settings and environment variables through the portal.
    ```bash
    func azure functionapp publish <functionappname>
    ```

### Deploy with publishing local function settings
* Deploy the function to azure and publish the function settings and environment variables.
    ```bash
    func azure functionapp publish <functionappname> --publish-local-settings
    ```
