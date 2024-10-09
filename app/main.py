from fastapi import FastAPI, HTTPException
import requests
from app.constants import API_URL

app = FastAPI()


@app.get("/ev-data/{model_year}")
def get_ev_data_by_year(model_year: int):

    response = requests.get(API_URL)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error fetching data from external API")

    data = response.json()

    filtered_data = [vehicle for vehicle in data if vehicle.get("model_year") == str(model_year)]

    if not filtered_data:
        raise HTTPException(status_code=404, detail="No data found for the specified model year")

    make_data = {}
    for vehicle in filtered_data:
        make = vehicle.get("make")
        electric_range = float(vehicle.get("electric_range", 0))

        if make not in make_data:
            make_data[make] = {"count": 0, "total_range": 0}

        make_data[make]["count"] += 1
        make_data[make]["total_range"] += electric_range

    result = []
    for make, stats in make_data.items():
        avg_range = stats["total_range"] / stats["count"]
        result.append({
            "make": make,
            "vehicle_count": stats["count"],
            "average_electric_range": avg_range
        })

    return result
