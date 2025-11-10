from datetime import date

import app.errors as error


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor.get("name")
        vaccine = visitor.get("vaccine")

        if not vaccine:
            raise error.NotVaccinatedError(name)

        if vaccine.get("expiration_date") < date.today():
            raise error.OutdatedVaccineError(name)

        if not visitor.get("wearing_a_mask", False):
            raise error.NotWearingMaskError(name)

        return f"Welcome to {self.name}"
