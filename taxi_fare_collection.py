def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10
    total_fare = base_fare + (distance_fare * distance)
    return total_fare

# input data
trips = [5, 10, 3]

# calculate fare for each trip
total_fare = 0
for i, trip in enumerate(trips, start=1):
    fare = calculate_fare(trip)
    total_fare += fare
    print(f"Trip {i}: ${fare}")

print(f"Total Fare: ${total_fare}")
