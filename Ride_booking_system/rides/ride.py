from utils.fare_calculator import FareCalculator


class Ride:

    ride_counter = 1

    def __init__(
        self,
        rider,
        driver,
        source,
        destination,
        distance,
        payment
    ):

        self.__ride_id = Ride.ride_counter
        Ride.ride_counter += 1

        self.__rider = rider
        self.__driver = driver
        self.__source = source
        self.__destination = destination
        self.__distance = distance
        self.__payment = payment

        self.__fare = FareCalculator.calculate_fare(distance)

        self.__status = "BOOKED"

    def start_ride(self):
        self.__status = "STARTED"
        print(f"Ride {self.__ride_id} started")

    def complete_ride(self):

        self.__payment.process_payment(self.__fare)

        self.__status = "COMPLETED"

        self.__rider.add_ride_history(self)

        print(f"Ride {self.__ride_id} completed")

    def cancel_ride(self):
        self.__status = "CANCELLED"
        print(f"Ride {self.__ride_id} cancelled")

    def get_ride_details(self):

        return {
            "ride_id": self.__ride_id,
            "source": self.__source,
            "destination": self.__destination,
            "distance": self.__distance,
            "fare": self.__fare,
            "status": self.__status
        }
