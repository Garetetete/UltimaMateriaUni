from fastapi import FastAPI, Response
from app.numbers import validate_number

app = FastAPI()

@app.get("/validate/{number}")
def validate_number_endpoint(number: str, response: Response):
    is_valid = validate_number(number)
    if is_valid:
        return {"number": number, "valid": True}
    else:
        response.status_code = 400
        return {"number": number, "valid": False, "error": "Invalid number format"}