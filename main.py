# Showroom main file
import pandas as pd


import cars
from cars import *
class ShowroomManagementSystem:
    CARS_CSV = "carsData.csv"
    @classmethod
    def add_car(cls):
        customer_name = input("Enter Your Name: ")
        print("\n\t\tWelcome to Car Registration Section\n")

        make = input("Enter Car Make: ")
        name = input("Enter Car Name: ")
        number = input("Enter Car Number: ")
        model = input("Enter Car Model: ")
        price = input("Enter Car Price: $")
        color = input("Enter Car Color: ")
        car_type = input("Enter Car Type (Press Enter for default 'Not Set'): ").strip()
        availability = input("Enter Car Availability: ")

        try:
            df = pd.read_csv(cls.CARS_CSV)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.CSV_COLUMNS)  # Create an empty DataFrame if file doesn't exist

            # Check if car number already exists
        if number in df["Number"].values:
            print(f"Error: Car with registration number {number} already exists.")
            return

        # Add car to the system
        Cars.add_car(number, make, name, model, price, color, car_type, availability)

        # Display all cars after registration
        print("\nUpdated Car List:")
        Cars.display_cars()

        print("Car is Registered")
        print(f"'{customer_name}' has registered Car {cars.Cars.car_name(name)}' ")

    @classmethod
    def remove_car(cls):
        CarRemove = "carsData.csv"
        # df = pd.read_csv("carsData.csv")
        df = pd.read_csv(CarRemove)
        print(df)
        remove_car = input("Enter Car Registration Number to Remove: ")

        # Check if the registration number exists in the column
        try:
            if remove_car in df["Number"].values:
                df = df[df["Number"] != remove_car]  # Remove the row where Number matches
                df.to_csv(CarRemove, index=False)
                print(f"Car with Registration Number '{remove_car}' was removed successfully.")
            else:
                print("Car Registration Number not found")
        except ValueError as e:
            print(f"Error: {e} Try Again.")

    @classmethod
    def display_car(cls):
        print("\n\t\t\tWelcome to Car DataBase Section")
        df = pd.read_csv("carsData.csv")
        filter_df = df[df["Number"] == df["Number"]]
        print(filter_df)

    @classmethod
    @classmethod
    def book_car(cls):
        print("\n\t\t\tWelcome to Car Booking Section")
        df = pd.read_csv("carsData.csv")
        print(df)

        book_a_car = input("\nEnter Car Registration Number to Book a Car: ")

        if book_a_car in df["Number"].values:
            # Check if the car is already booked
            if df.loc[df["Number"] == book_a_car, "Availability"].values[0] == "Booked":
                print(f"Sorry, the car {book_a_car} is already booked.")
            else:
                df.loc[df["Number"] == book_a_car, "Availability"] = "Booked"
                df.to_csv("carsData.csv", index=False)  # Save changes to CSV
                print(f"{book_a_car} was booked successfully.")
        else:
            print(f"{book_a_car} was not found in the database. Please try again.")

    @classmethod
    def filter_by_price(cls):
        df = pd.read_csv("carsData.csv")

        minpricerange = input("Enter Your Minimum Price Range that you looking For: $")
        maxpricerange = input("Enter Your Maximum Price Range that you looking For: $")

        # Remove the $ sign and convert prices to float
        df["Price"] = df["Price"].replace('[\$,]', '', regex=True).astype(float)
        minpricerange = float(minpricerange)
        maxpricerange = float(maxpricerange)

        mask = (df["Price"] >= minpricerange) & (df["Price"] <= maxpricerange)
        filtered_df = df.loc[mask]
        if filtered_df.empty:
            print(f"No cars were found for '${minpricerange}' to '${maxpricerange}' range.")
        else:
            print(filtered_df)


if __name__ == '__main__':
    while True:
        print("\n\t\tWelcome to 'SAYAB's ShowRoom'")

        print("1. For Car Registration Section")
        print("2. For Removing Car from DataBase")
        print("3. For Car Booking Section")
        print("4. For View Car's In DataBase")
        print("5. Filter Car Prices")
        print("6. For Exit")

        choice = input("Enter Your Choice between 1 to 6: ")
        if choice == "1":
            ShowroomManagementSystem.add_car()
        elif choice == "2":
            ShowroomManagementSystem.remove_car()
        elif choice == "3":
            ShowroomManagementSystem.book_car()
        elif choice == "4":
            ShowroomManagementSystem.display_car()
        elif choice == "5":
            ShowroomManagementSystem.filter_by_price()
        elif choice == "6":
            print("Thank You For Choosing 'SAYAB's ShowRoom'")
            break
        else:
            print("Invalid Input, Please Enter 1 to 7...")