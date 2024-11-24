# Use official Python 3.10 image as the base
FROM python:3.10.0-slim

# Install system dependencies for Node.js and other tools
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*




# Install Node.js (specifically the version needed)
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs git nano\
    && rm -rf /var/lib/apt/lists/*


    # Install Rust (and cargo)
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | bash -s -- -y

# Add cargo to PATH by modifying the shell profile
RUN export PATH="$HOME/.cargo/bin:$PATH"
RUN echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc



# Set the working directory to the app directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app


