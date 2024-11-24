
# ZK Circuit Project

  

This project involves the development and testing of cryptographic circuits. To run the project, please ensure that your system meets the following requirements and follow the setup instructions.

  

## System Requirements

  

-  **RAM**: At least 16 GB of RAM is required to run this project effectively. If you have lower RAM, performance may be significantly impacted.

  

## Docker Setup (Recommended)

  

For easy environment setup, we provide a Docker image that contains all the dependencies required to run the project.

  

### Docker Image

  

The Docker image for this project is available under the name `harshu4/zk_circuit_project`.

  

### Steps to Run the Project using Docker

  

1.  **Pull the Docker Image**:

  

To pull the Docker image, run the following command:

  

```bash

docker pull harshu4/zk_circuit_project

```

  

2.  **Run the Docker Image**:

  

To start a container from the image, run:

  

```bash

docker run -it harshu4/zk_circuit_project

```

  

3.  **Enter the Docker Container**:

  

Once inside the container, navigate to the project directory (if not already there) and run the following command to start the test:

  

```bash

python test.py

```

  

This will run the test and display the results.

  

## Manual Setup (If Docker is not preferred)

  

If you prefer to set up the environment on your main host machine, please follow the steps below.

  

### 1. Install Python 3.10.0

  

To install Python 3.10.0, run the following commands:

  

-  **On Ubuntu**:

  

```bash

sudo apt update

sudo apt install python3.10

```

  

-  **On macOS**:

  

You can use Homebrew to install Python 3.10.0:

  

```bash

brew install python@3.10

```

  

### 2. Install Node.js

  

Next, you need to install Node.js. You can install Node.js by following these steps:

  

-  **On Ubuntu**:

  

```bash

sudo apt update

sudo apt install nodejs npm

```

  

-  **On macOS**:

  

You can install Node.js using Homebrew:

  

```bash

brew install node

```

  

### 3. Run the Setup Script

  

After installing Python and Node.js, you can set up the environment by running the following commands:

  

```bash

sh  setup-circom.sh

npm  install

pip  install  -r  requirements.txt

python test.py