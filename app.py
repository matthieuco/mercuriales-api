from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import tempfile
from datetime import date
import os


from mercuriales import (
    build_dataframe,
    build_average_dataframe,
    export_excel
)

app = FastAPI()

@app.get("/")
def healthcheck():
    return {
        "status": "ok"
    }

@app.post("/convert")
async def convert(
    forains_pdf: UploadFile = File(...),
    gms_pdf: UploadFile = File(...)
):

    today = date.today().strftime("%Y%m%d")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpf:

     tmpf.write(await forains_pdf.read())

     forains_path = tmpf.name
     forains_df = build_dataframe(forains_path)


    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpg:

     tmpg.write(await gms_pdf.read())

     gms_path = tmpg.name
     gms_df = build_dataframe(gms_path)


    average_df = build_average_dataframe(
        forains_df,
        gms_df
    )

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".xlsx"
    ) as tmpx:

        output_file = tmpx.name

    if os.path.exists(output_file):
        os.remove(output_file)

    export_excel(
        forains_df,
        gms_df,
        average_df,
        output_file
    )

    return FileResponse(
        output_file,
        filename=f"mercuriales_{today}.xlsx",
        media_type=
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )