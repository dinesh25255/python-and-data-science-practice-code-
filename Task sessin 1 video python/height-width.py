# Get dimensions of the milk tank from the user
height = float(input("Enter the height of the milk tank (in cm): "))
width = float(input("Enter the width of the milk tank (in cm): "))
breadth = float(input("Enter the breadth of the milk tank (in cm): "))

# Get the volume of one glass from the user
glass_volume = float(input("Enter the volume of one glass (in cubic cm): "))

# Calculate the volume of the milk tank
tank_volume = height * width * breadth

# Calculate the number of glasses that can be filled
number_of_glasses = tank_volume // glass_volume  # Use integer division for whole glasses

# Output the result
print(f"The number of glasses of milk that can be obtained is: {int(number_of_glasses)}")
