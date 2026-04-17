def get_advisory(rainfall, temperature):
    # Irrigation check
    if rainfall < 200:
        return "Advisory: Irrigation Required"
    
    #  High heat check (Nested logic)
    elif temperature > 30:
        return "Advisory: Monitor Soil"
    
    
    else:
        return "Advisory: Normal Conditions"


rain = float(input("Enter rainfall (mm): "))
temp = float(input("Enter temperature (°C): "))
print(get_advisory(rain, temp))