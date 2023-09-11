import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

#view structure data

Cars = pd.read_csv('Session_4\Car_cat.csv')
print(Cars.head())

#clean the dat   a and get the most expensive data
Cars = pd.read_csv('Session_4\Car_cat.csv')
Cars = Cars.drop_duplicates(subset='model', keep='last')

Highestprice =Cars.loc [ Cars['price'].idxmax()]

car_name = Highestprice['model']
car_price = Highestprice['price']

print("================= PAGE BREAKER =======================")


print(car_name,"is the most expensive car at £",car_price)


print("================= PAGE BREAKER =======================")



#Get the avarage price for the VW Golf models

# Read the CSV file into a DataFrame
car_data = pd.read_csv('Session_4\Car_cat.csv')  

# Filter the DataFrame for VW Golf models
vw_golf_models = car_data[car_data['model'].str.contains('Golf', case=False).notna()]

# Calculate the average price
average_price = vw_golf_models['price'].mean()

print("The average price for the VW Golf Models is £",average_price)
print("================= PAGE BREAKER =======================")


#average milage for VW Polo models registered in 2020?



# Read the CSV file into a DataFrame
car_data = pd.read_csv('Session_4\Car_cat.csv')  

# Filter the DataFrame for VW Polo models from the year 2020
vw_polo_models = car_data[(car_data['model'].str.contains('Polo', case=False, na=False)) & (car_data['year'] == 2020)]

# Group the filtered DataFrame by 'model' and count the 'mileage'
result = vw_polo_models.groupby('model')[['mileage']].count()

# Reset the index to make 'model' a column again
result.reset_index(inplace=True)

# Display the result
print(result)
print("================= PAGE BREAKER =======================")

average_mileage = vw_polo_models['mileage'].mean()
print("The average mileage for the POLO as of  2020 is MPG", average_mileage)

print("================= PAGE BREAKER =======================")
print("========== All models and their average Mileage ===========")

# A bar chart showing the average mileage for each model. (You need to research hpow can you calculate average using pandas

# Read the CSV file into a DataFrame
Cars = pd.read_csv('Session_4\Car_cat.csv')  
Cars = Cars.drop_duplicates(subset='model', keep='last')

# Group the filtered DataFrame by 'model' and mean the 'mileage'
result_forall = Cars.groupby('model')[['mileage']].mean()
#sort the values
result_forall = result_forall.sort_values(by='model', ascending=True)
# Reset the index to make 'model' a column again
result_forall.reset_index(inplace=True)

print(result_forall)
print("================= PAGE BREAKER =======================")
print("========== All models and their fuel type ===========")

#A pie chart showing the distribution between fuel types. (You can use the model column to count occurances!)


Cars = pd.read_csv('Session_4\Car_cat.csv')  
Cars = Cars.drop_duplicates(subset='model', keep='last')


# Group the DataFrame by 'model' and 'fuelType' to get unique combinations
result_forall_fuel = Cars.groupby(['model', 'fuelType']).size().reset_index(name='Count')

# Print the DataFrame to display models and their associated fuel types
print(result_forall_fuel)

# Group the DataFrame by 'fuelType' and count the occurrences of each fuel type
fuel_type_counts = Cars['fuelType'].value_counts()



#Plotting the bar chat
# using the style for the plot
plt.style.use('dark_background')

plt.bar(result_forall['model'], result_forall['mileage'], color='maroon', width=0.4)
plt.xlabel("Car Models")
plt.ylabel("Average Mileage")
plt.title("The Average Mileage for Each Model")

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha="right")  # Adjust the rotation angle as needed

plt.tight_layout()  # Ensures the labels are not cut off
plt.show()


#plotting the pie chart
# Defining colors for the pie chart
colors = ['pink', 'silver', 'steelblue']

plt.pie(fuel_type_counts, labels=fuel_type_counts.index, autopct='%1.1f%%',colors=colors, startangle=140)
plt.style.use('dark_background')

# Add a title
plt.title('Pie Chart Showing Fuel Type Distribution')

# Show the chart
plt.show()

