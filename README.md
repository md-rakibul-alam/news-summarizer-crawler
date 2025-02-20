# News Summarizer Back-End

## Running with Docker

1. Ensure Docker is installed on your machine. You can download it from [here](https://www.docker.com/products/docker-desktop).

2. Navigate to the project directory:
    ```sh
    cd /d:/PersonalProjects/news-summarizer/back-end
    ```

3. Create a `.env` file in the same directory with the following environment variables:
    ```env
    MONGO_DB=news_summarizer
    MONGO_PORT=27017
    MONGO_EXPRESS_PORT=8081
    MONGO_EXPRESS_USER=admin
    MONGO_EXPRESS_PASSWORD=new_secure_password
    PORT=8000
    GEMINI_API_KEY=AIzaSyAC-_IhAXPdVAuPHqZEpBs8Q3yr8QH2G6I
    ```

4. Run the following command to start the services:
    ```sh
    docker-compose up
    ```

5. Access the application:
    - The app will be available at `http://localhost:8001`
    - Mongo Express will be available at `http://localhost:8081`

6. To stop the services, press `Ctrl+C` in the terminal where the services are running, and then run:
    ```sh
    docker-compose down
    ```
