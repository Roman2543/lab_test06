from fastapi import APIRouter

years_api_router = APIRouter()

@years_api_router.get("/service/getage")
async def get_test(year: int):
        if(year<=0):
            return{"age":"Your input lower"}
        elif(year>2565):
            return{"age":"Your input higher"}
        return {"age": 2565 -year}
