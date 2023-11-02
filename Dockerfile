# Use an official base image
FROM dealii/dealii:v9.4.0-focal


# Install software or run other commands
RUN sudo apt-get update && sudo apt-get install -y python3 python3-pip

# Copy application code or files into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Run the CMake build process
RUN sudo cmake . && sudo make

# Specify the command to run when the container starts
CMD ["sudo", "python3", "auto_file.py", "2"]
