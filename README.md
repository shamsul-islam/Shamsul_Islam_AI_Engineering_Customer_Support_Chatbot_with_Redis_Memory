# Customer Support Chatbot with Redis Memory

This is a simple customer support chatbot that uses Redis to store chat history and improve context understanding over time.

## Features

*   Answers frequently asked questions (FAQs).
*   Stores chat history for each user in Redis.
*   Provides a simple REST API for interacting with the chatbot.

## Project Structure

```
.gitignore
app.py
config.py
requirements.txt
README.md
Dockerfile
docker-compose.yml
```

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/shamsul-islam/Shamsul_Islam_AI_Engineering_Customer_Support_Chatbot_with_Redis_Memory.git
    cd Shamsul_Islam_AI_Engineering_Customer_Support_Chatbot_with_Redis_Memory
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Start Redis (Optional, if not using Docker Compose):**

    If you are running the application directly (i.e., `python app.py`), ensure you have Redis installed and running on `localhost:6379`. If you are using Docker Compose, this step is not necessary as Redis will be managed by Docker.
4.  **Run the application:**

    ```bash
    python app.py
    ```

## Running with Docker

If you have Docker installed, you can easily run the application and Redis with a single command. This is the recommended way to run the project as it doesn't require you to install Redis on your machine.

```bash
docker-compose up
```

## Usage

You can interact with the chatbot by sending POST requests to the `/chat` endpoint.

**Request:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"user_id": "123", "message": "What are your business hours?"}' http://127.0.0.1:5000/chat
```

**Response:**

```json
{
  "response": "Our business hours are 9 AM to 5 PM, Monday to Friday."
}
```

**Testing with PowerShell:**

On Windows, you can use the provided PowerShell script to send a test message:

```powershell
.\send_chat.ps1
```

## Contributing

### Pushing Changes to Remote

If you make changes to the project and want to push them to your remote GitHub repository, follow these steps:

1.  **Stage your changes:**
    ```bash
    git add .
    ```
2.  **Commit your changes:**
    ```bash
    git commit -m "Your descriptive commit message here"
    ```
3.  **Push to the remote repository:**
    ```bash
    git push origin main
    ```
    (Replace `main` with your branch name if it's different, e.g., `master`.)
