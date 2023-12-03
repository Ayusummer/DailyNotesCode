from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

# 设置一个文件夹来存储上传的文件
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIRECTORY = BASE_DIR / "uploads"
UPLOAD_DIRECTORY.mkdir(exist_ok=True)

# 静态文件和模板
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    files = [file.name for file in UPLOAD_DIRECTORY.iterdir() if file.is_file()]
    return templates.TemplateResponse(
        "index.html", {"request": request, "files": files}
    )


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_location = UPLOAD_DIRECTORY / file.filename
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}


@app.get("/download/{filename}")
async def download_file(filename: str):
    file_location = UPLOAD_DIRECTORY / filename
    if file_location.exists():
        return FileResponse(str(file_location))
    return {"error": "File not found"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
