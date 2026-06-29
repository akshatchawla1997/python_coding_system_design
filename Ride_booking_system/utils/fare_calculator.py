class FareCalculator:
    @staticmethod
    def calculate_fare(distance, base_fare=5, per_km_rate=2):
        """
        Calculate the fare based on distance.
        
        :param distance: Distance of the ride in kilometers.
        :param base_fare: Base fare for the ride.
        :param per_km_rate: Rate per kilometer.
        :return: Total fare for the ride.
        """
        return base_fare + (distance * per_km_rate)
    