# November 19, 2023
# Sal's Shipping Project

weight = 41.5
shipping_cost = 20
ground_shipping_premium_cost = 125.00

print("Package Weight: "+ str(weight))

# Ground Shipping
if weight <= 2.0:
  shipping_cost = (1.50 * weight) + (20)
elif weight > 2.0 and weight <= 6.0:
  shipping_cost = (3.00 * weight) + 20
elif weight > 6.0 and weight <= 10.0:
  shipping_cost = (4.00 * weight) + 20
else:
  shipping_cost = (4.75 * weight) + 20

print("Ground Shipping: " + str(shipping_cost))
print("Premium Shipping: " + str(ground_shipping_premium_cost))

# Drone Shipping
if weight <= 2.0:
  shipping_cost = (4.50 * weight) 
elif weight > 2.0 and weight <= 6.0:
  shipping_cost = (9.00 * weight)
elif weight > 6.0 and weight <= 10.0:
  shipping_cost = (12.00 * weight) 
else:
  shipping_cost = (14.25 * weight)

print("Drone Shipping: " + str(shipping_cost))
