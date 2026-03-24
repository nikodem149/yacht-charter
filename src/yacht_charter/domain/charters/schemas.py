from pydantic import BaseModel, model_validator, field_validator
from datetime import date, datetime

CHARTER_REQUEST_KEYS_MAPPER = {"startDate": "start_date", "endDate": "end_date"}

class CharterRequest(BaseModel):
    start_date: date
    end_date: date
    boat_id: int | None = None


    @model_validator(mode="before")
    @classmethod
    def camels_to_snakes(cls, data: dict):
        return {CHARTER_REQUEST_KEYS_MAPPER.get(key,key): value for key, value in data.items()}


    @field_validator("start_date", mode="before")
    @classmethod
    def start_date_format(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%d.%m.%Y").date()
        return value

    @model_validator(mode="after")
    def validate_dates(self) -> 'CharterRequest':
        if self.start_date >= self.end_date:
            raise ValueError("Start date must be before end date")
        if self.start_date < date.today():
            raise ValueError("Start day cannot be before today")
        return self



if __name__ == "__main__":
    charter_request = CharterRequest.model_validate(
        {"startDate": "12.03.2030", "endDate": date(2030,4,12)})
    print(charter_request.start_date)
    print(charter_request.end_date)
