from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/chart/latest")
def get_latest_chart():
    return FileResponse("chart_EURUSD M15 Chart.png")
