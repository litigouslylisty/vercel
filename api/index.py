from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["GET"],  # Allow GET requests
    allow_headers=["*"],  # Allow all headers
)

# Load marks from CSV
def load_marks():
    marks = {}
    with open("marks.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            marks[row["name"]] = int(row["marks"])
    return marks

marks_data = load_marks()

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    result = [marks_data.get(n, 0) for n in name]
    return {"marks": result}
