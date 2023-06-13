from typing import Any, List, Optional

from pydantic import BaseModel
from regression_model.processing.validation import DataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "Location1": "Bahria Apartments, Bahria Town Karachi",
                        "Type": "Flat",
                        "Bedrooms": 4.0,
                        "Bathrooms": 4.0,
                        "Size_in_SqYds": 328.0,
                        # "Price_in_millions": 28.0,
                        "Parking_Spaces": 1,
                        "Floors_in_Building": 2.0,
                        "Elevators": 1,
                        "Lobby_in_Building": 0,
                        "Double_Glazed_Windows": 0,
                        "Central_Air_Conditioning": 0,
                        "Central_Heating": 0,
                        "Waste_Disposal": 0,
                        "Furnished": 0,
                        "Service_Elevators_in_Building": 0,
                        "Flooring": 1,
                        "Electricity_Backup": 1,
                        "Servant_Quarters": 0,
                        "Study_Room": 0,
                        "Prayer_Room": 0,
                        "Powder_Room": 0,
                        "Gym": 0,
                        "Lounge_or_Sitting_Room": 0,
                        "Laundry_Room": 0,
                        "Business_Center_or_Media_Room_in_Building": 0,
                        "Satellite_or_Cable_TV_Ready": 1,
                        "Broadband_Internet_Access": 1,
                        "Intercom": 1,
                        "Conference_Room_in_Building": 0,
                        "Community_Swimming_Pool": 0,
                        "Community_Lawn_or_Garden": 0,
                        "Community_Gym": 0,
                        "Community_Center": 0,
                        "First_Aid_or_Medical_Centre": 0,
                        "Day_Care_center": 0,
                        "Kids_Play_Area": 0,
                        "Mosque": 0,
                        "Barbeque_Area": 0,
                        "Lawn_or_Garden": 0,
                        "Swimming_Pool": 0,
                        "Sauna": 0,
                        "Jacuzzi": 0,
                        "Nearby_Schools": 0,
                        "Nearby_Hospital": 0,
                        "Nearby_Shopping_Malls": 0,
                        "Nearby_Restaurants": 0,
                        "Nearby_Public_Transport_Service": 0,
                        "Other_Nearby_Places": 0,
                        "Security_Staff": 0,
                        "Maintainance_Staff": 0,
                        "Laundry_or_Dry_Cleaning_Facility": 0,
                        "Facilities_for_Disabled": 0,
                        # this one is only to calculate temporal variable:
                        "Built_in_year_year": 2023,
                    }
                ]
            }
        }