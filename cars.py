import csv
import pandas as pd

class Cars:
    cars = []  # Store list of car dictionaries
    CARS_CSV = "carsData.csv"
    CSV_COLUMNS = ["Number", "Make", "Name", "Model", "Price", "Color", "Car Type", "Availability"]

    @classmethod
    def load_csv(cls):
        try:
            df = pd.read_csv(cls.CARS_CSV)
            if df.empty:
                df.to_csv(cls.CARS_CSV, index=False)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.CSV_COLUMNS)
            df.to_csv(cls.CARS_CSV, index=False)

    @classmethod
    def car_name(cls, name):
        return name  # Keeping method for potential use

    @classmethod
    def car_make(cls, make):
        return make

    @classmethod
    def car_model(cls, model):
        return model

    @classmethod
    def car_number(cls, number):
        return number

    @classmethod
    def car_price(cls, price):
        return f"${str(price).strip()}"

    @classmethod
    def car_color(cls, color):
        return color

    @classmethod
    def car_type(cls, car_type):
        return car_type if car_type.strip() else "Not Set"  # Default to 'Not Set' if empty

    @classmethod
    def car_availability(cls, availability):
        return availability

    @classmethod
    def add_car(cls,number, make, name, model, price, color, car_type, availability):
        #  Check if the car number already exists

        # Check if the CSV file exists
        try:
            df = pd.read_csv(cls.CARS_CSV)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.CSV_COLUMNS)  # Create an empty DataFrame if the file is missing

        # Check if the "Number" column exists
        if "Number" not in df.columns:
            df = pd.DataFrame(columns=cls.CSV_COLUMNS)  # Reset columns if missing

        # Check if the car number already exists (Primary Key Constraint)
        if number in df["Number"].values:
            print(f"Error: Car with registration number {number} already exists.")
            return

        new_entry = {
            "Number": cls.car_name(number),
            "Make": cls.car_make(make),
            "Name": cls.car_name(name),
            "Model": cls.car_model(model),
            "Price": cls.car_price(price),
            "Color": cls.car_color(color),
            "Car Type": cls.car_type(car_type),
            "Availability": cls.car_availability(availability),
        }

        # Store in class list
        cls.cars.append(new_entry)

        # Save to CSV
        with open(cls.CARS_CSV, 'a', newline="") as carfile:
            writer = csv.DictWriter(carfile, fieldnames=cls.CSV_COLUMNS)
            if carfile.tell() == 0:
                writer.writeheader()
            writer.writerow(new_entry)

        print(f"Car '{name}' was added successfully.")

    @classmethod
    def display_cars(cls):
        """Prints the list of cars in a readable format."""
        if not cls.cars:
            print("No cars available.")
        else:
            for car in cls.cars:
                print(car)


# Cars.add_car("ICT-234","Toyota", "Corolla Grande", "2022", 7100, "Black", "Sedan", "Available")
# Cars.add_car("LHR-873","Honda", " X", "2020", 4500, "White", "Sedan", "Available")
# Cars.add_car("ICT-333", "Ford", "Raptor", "2019", 4500, "Blue", "", "Booked")
# Cars.add_car("ICT-1", "BMW", "X5", "2023", 15000, "Gray", "SUV", "Available")
#
# print(Cars.display_cars())  # Now this should correctly store car dictionaries
