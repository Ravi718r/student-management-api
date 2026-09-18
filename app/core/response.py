from app.schemas.common import SuccessResponse

def success_response(
        data= None,
        message = " Success"
):
    return SuccessResponse(
        success= True,
        message= message,
        data=data
    )