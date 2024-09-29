# Use the official Node.js image as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY frontend/package*.json ./frontend/

# Install dependencies
RUN npm install --prefix ./frontend

# Copy the rest of the application code
COPY frontend/ ./frontend/

# Expose the application port
EXPOSE 3000

# Command to run the application
CMD ["npm", "start", "--prefix", "./frontend"]
