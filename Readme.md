Spatial API - Django & DRF

This project provides APIs for handling spatial data using Django, Django Rest Framework (DRF), and PostGIS. The API supports Point, MultiPoint, and Polygon operations using GET, POST, and PUT methods.

📌 Installation Guide

1️⃣ Clone the Repository

git clone <repository_url>
cd <project_directory>

2️⃣ Create & Activate Virtual Environment

python3 -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

or 
use the present venv and activate 

using source venv/bin/activate  

4️⃣ Run the Development Server

python manage.py runserver

The API will be available at: http://127.0.0.1:8000/

🚀 API Endpoints & Usage

Spatial Points API

Method

Endpoint

Description

GET

/api/spatialpoints/

Get all spatial points

POST

/api/spatialpoints/

Create a new spatial point

PUT

/api/spatialpoints/{id}/

Update an existing spatial point

Example Payloads

✅ POST (Create Point)

{
    "name": "Point A",
    "location": { "type": "Point", "coordinates": [77.5946, 12.9716] }
}

✅ PUT (Update Point)

{
    "name": "Updated Point A",
    "location": { "type": "Point", "coordinates": [78.4867, 17.3850] }
}

Spatial Polygons API

Method

Endpoint

Description

GET

/api/spatialpolygons/

Get all polygons

POST

/api/spatialpolygons/

Create a new polygon

PUT

/api/spatialpolygons/{id}/

Update an existing polygon

Example Payloads

✅ POST (Create Polygon)

{
    "name": "Polygon Area",
    "area": {
        "type": "Polygon",
        "coordinates": [
            [
                [77.5946, 12.9716],
                [78.4867, 17.3850],
                [79.1234, 18.9876],
                [77.5946, 12.9716]  // Closed loop (first == last)
            ]
        ]
    }
}

✅ PUT (Update Polygon)

{
    "name": "Updated Polygon Area",
    "area": {
        "type": "Polygon",
        "coordinates": [
            [
                [75.1234, 15.5678],
                [76.6543, 16.8765],
                [77.2345, 14.4567],
                [75.1234, 15.5678]  // Closed loop
            ]
        ]
    }
}

🎯 Running Tests

To verify that everything is working correctly:

Test the api endpoints using postman or any api testing tools
