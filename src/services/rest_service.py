from fastapi import HTTPException, status


def bad_request(exception: BaseException):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Error: {}".format(exception)
    )
