pip install fastapi
pip install "uvicorn[standard]"

RUN WITH
uvicorn main:app --reload
