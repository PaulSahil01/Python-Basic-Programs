def calculate_taxi_fare(distance):
  cost_per_km = 1.5
  hst_rate = 0.18
  base_fare = distance * cost_per_km
  final_fare = base_fare * (1 + hst_rate)
  return final_fare

distance = float(input("Enter the distance in kilometers: "))
final_price = calculate_taxi_fare(distance)
print(f"The final taxi fare including 18% HST is: ${final_price:.2f}")