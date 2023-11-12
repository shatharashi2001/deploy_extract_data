import io
from fastapi import File, UploadFile, APIRouter, Response
from errors import *
import uuid
import nest_asyncio
from extracts import get_extr_data


nest_asyncio.apply()

router = APIRouter()


@router.post("/get_data/")
async def extracts(response: Response, string_ex: str, req_id: str = None):
    try:
        output_data = get_extr_data(string_ex)
        return output_data

    except FileNotFoundError:
        exc_message = handle_exception(custom_exc=FileNotFoundError)
        response.status_code = FileNotFoundError.code
        error_message = f"{FileNotFoundError.code} {FileNotFoundError.description}"
        return {"req_id": req_id, "error": {"message": exc_message}}

    except FileNotAcceptedError:
        exc_message = handle_exception(custom_exc=FileNotAcceptedError)
        response.status_code = FileNotAcceptedError.code
        error_message = (
            f"{FileNotAcceptedError.code} {FileNotAcceptedError.description}"
        )
        return {"req_id": req_id, "error": {"message": exc_message}}
