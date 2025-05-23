print("Temperature Conversion\n\nI would like to convert a temperature value from one unit to another, specifically between degrees Celsius (°C) and degrees Fahrenheit (°F). Could you please assist me with the conversion?\n") 
print("Conversion Options\n\nTo proceed, please select one of the following options:\n") 
print("- Press 1 to convert to °C (Celsius)\n- Press 2 to convert to °F (Fahrenheit)")
try :    
    user_choice = int(input("\n>>> "))
    if (user_choice == 1) :
        celcius_input = int(input('Enter the value in degrees Celsius (°C): '))
        fahrenheit_output = (9/5 * celcius_input) + 32
        print(f"{celcius_input} degrees Celsius is equal to {fahrenheit_output} degrees Fahrenheit")
    elif (user_choice == 2) :
        fahrenheit_input = int (input("Enter the value in degrees Fahrenheit (°F)>>>"))
        celcius_output = (fahrenheit_input - 32) * 5/9
        print (f"{fahrenheit_input} degrees Fahrenheit is equal to {celcius_output} degrees Celcius")
except Exception as e :
    print(f"Sorry!! Some error occurred\nError : {e}")