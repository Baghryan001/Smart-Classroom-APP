from fastapi import APIRouter, File, UploadFile, HTTPException, status
from server.services.face_detector import detect_faces
from server.models.schemas import ProcessFrameResponse, HealthCheckResponse

router = APIRouter(prefix="/vision", tags=["Vision Processing"])

latest_detection = {
    "status": "no_data_yet",
    "filename": None,
    "faces_detected": 0,
}


@router.get(
    "/latest-result", summary="Get the latest frame detection result"
)
def get_latest_result():
    return latest_detection


@router.get(
    "/health",
    response_model=HealthCheckResponse,
    summary="Check Vision module status",
)
def health_check():
    return HealthCheckResponse(status="Vision module is working")


@router.post(
    "/process-frame",
    response_model=ProcessFrameResponse,
    summary="Process the camera footage and count faces",
    status_code=status.HTTP_200_OK,
)
async def process_frame(file: UploadFile = File(...)):
    global latest_detection

    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Please send only an image (image/jpeg, image/png):",
        )

    try:
        contents = await file.read()

        if len(contents) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The sent file is empty:",
            )

        faces_count = detect_faces(contents)

        if faces_count == -1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The file is corrupt or cannot be decoded as an image:",
            )

   
        latest_detection = {
            "status": "success",
            "filename": file.filename or "frame.jpg",
            "faces_detected": faces_count,
        }

        # 2. Տպում ենք սերվերի տերմինալում
        print(f"[SERVER] Frame received | Faces detected: {faces_count}")

        return ProcessFrameResponse(
            status="success", filename=file.filename, faces_detected=faces_count
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Server error while processing the image. {str(e)}",
        )
