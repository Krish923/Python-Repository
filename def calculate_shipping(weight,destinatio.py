def calculate_shipping(weight,destination):
    if (weight>=1.0 and weight<=1000.0) :
        if len(destination)>=1 and len(destination)<=15: 
            return weight*destination
weight = float(input())
destination = input()
shipping_cost = calculate_shipping(weight, destination)
if shipping_cost is not None:
    print(f"Shipping cost to {destination} for a {weight} kg package: {shipping_cost:.2f}")        