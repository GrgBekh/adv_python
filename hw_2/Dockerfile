# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src ./src

# Install pdflatex and necessary dependencies
RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir LatexGenerationCustomLibrary

