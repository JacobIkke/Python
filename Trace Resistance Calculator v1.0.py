# Simple PCB Trace Resistance Calculator

def calculate_trace_resistance(width_mils, length_mm, thickness_um, temperature_C):
    # local Constants
    rho_20 = 1.68e-8  	# Resistivity of copper at 20°C in ohm meters 
    alpha = 0.00386  	# Temperature coefficient of resistivity for copper
    
    # Convert units
    width_m = width_mils * 2.54e-5  	# Convert width from mils to meters
    length_m = length_mm * 1e-3  		# Convert length from mm to meters
    thickness_m = thickness_um * 1e-6  	# Convert thickness from um to meters
    
    # Calculate cross-sectional area
    area_m2 = width_m * thickness_m
    
    # Adjust resistivity for ambient temperature
    rho_T = rho_20 * (1 + alpha * (temperature_C - 20))
    
    # Calculate the final resistance
    resistance_ohms = (rho_T * length_m) / area_m2
    
    return resistance_ohms

# Example usage
width_mils = 12  	# Example width in mils
length_mm = 10  	# Example length in mm
thickness_um = 35  	# Example thickness in um
temperature_C = 25  # Example temperature in °C

resistance = calculate_trace_resistance(width_mils, length_mm, thickness_um, temperature_C)
print(f"Trace Resistance: {resistance:.6f} ohms")
