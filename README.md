# HICC Media API

FastAPI + Supabase + Redis backend for a scheduling application (specifically for a volunteer church media team)

## Architecture

-   [Fast API](https://fastapi.tiangolo.com/) - Python web framework for the API
-   [Supabase](https://supabase.com/) - Hosted PostgreSQL database
-   [Redis](https://redis.io/) via [Upstash](https://upstash.com/) - Hosted caching database

## Getting Started / Installation

1. Clone this repo
2. Create and activate Python virtual environment (this project uses v3.13.3)
3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
4. Configure environment variables
    - `.env`
        - `SUPABASE_URL`
        - `SUPABASE_API_KEY`
    - `test.env`
        - `SUPABASE_TEST_URL`
        - `SUPABASE_TEST_API_KEY`
5. Run tests (optional)
    ```bash
    pytest
    ```
6. Run dev server
    ```bash
    fastapi dev app/main.py
    ```
    - Server is running on localhost:8000
    - Docs are availabile at localhost:8000/docs

## Roadmap

-   [x] Design and launch PostgreSQL database on Supabase
-   [x] Create FastAPI that runs CRUDs on Supabase DB
-   [x] Implement unit testing and integration testing for all routes
-   [ ] Implement Redis as a cache
-   [ ] Create an auto-scheduling algorithm
