# Carly's Clippers Exercise
# November 21, 2023

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

combined_data = zip(hairstyles,prices,last_week)

# Sum the total of prices above.
total_price = 0 
for i in prices:
    total_price += i
print(total_price)

average_price = total_price/len(prices)

print("Average Haircut Price: ")
print(average_price)

#the average was too high, so cutting all prices by 5
new_prices = [i - 5 for i in prices]
print(new_prices)

# calculate total revenue by multiplying each price by the frequency last week
total_revenue = 0 
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

# then do the average
average_daily_revenue = total_revenue/7
print("Average Daily Revenue: " + str(average_daily_revenue))

#only show those hairstyles with prices under 30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)