from fastapi import APIRouter

router = APIRouter()

@router.get('/example')
def get_example():
    return {"example_key": "example_value"}

@router.post('/example')
def create_example(data: dict):
    return {"message": "Data received", "data": data}
