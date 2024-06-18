# Use Case App

This repository contains a web application built with FastAPI for predicting product tier and detail views based on car data. It includes both classification and regression models trained on car data attributes.

## Getting Started

### Prerequisites

- Docker installed on your system

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/befawzy/use_case_app.git
   cd use_case_app
2. Build the Docker image:

   ```bash
   docker build -t autoscout-app .

3. Run the Docker container:

    ```bash
   docker run -d -p 8000:8000 autoscout-app

4. The FastAPI application should now be accessible at http://localhost:8000.   
