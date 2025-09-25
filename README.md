Under Development
# LangGraph Backend

## Setup

1. Create and activate a virtual environment:
    ```
    python -m venv venv
    venv\Scripts\activate  # On Windows
    ```

2. Install dependencies:
    ```
    pip install -r ../requirements.txt
    ```

3. Run the server:
    ```
    uvicorn app.main:app --reload
    ```

## API

- `POST /process`  
  **Body:** `{ "prompt": "your text here" }`  
  **Response:** `{ "result": "Processed: your text here" }`

## Development

- To format code, run: `black .`
- To check type annotations, run: `mypy .`

- To run tests, use: `pytest`
