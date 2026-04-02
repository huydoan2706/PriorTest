class Citizen:
    def __init__(self, id, last_name, middle_name, first_name, hometown, living_area):
        self.id = id
        self.last_name = last_name
        self.middle_name = middle_name
        self.first_name = first_name
        self.hometown = hometown
        self.living_area = living_area

    def get_full_name(self):
        return f"{self.last_name} {self.middle_name} {self.first_name}"

    def get_hometown_id(self):
        return f"{self.hometown.id}"

    def get_hometown_name(self):
        return f"{self.hometown.name}"

    def get_living_area_id(self):
        return f"{self.living_area.id}"

    def get_living_area_name(self):
        return f"{self.living_area.name}"
