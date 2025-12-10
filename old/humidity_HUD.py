import serial
import json
import pandas as pd
import pygame
from pygame.locals import *

# Setup pygame
pygame.init()
window = pygame.display.set_mode((1600, 1200))
font = pygame.font.Font(None, 36)

ser = serial.Serial('/dev/ttyACM0', 9600)  # replace '/dev/ttyACM0' with your Arduino's port
df = pd.DataFrame()

while True:
    # Pygame event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    try:
        line = ser.readline().decode('utf-8').strip()  # read a '\n' terminated line
        data = json.loads(line)

        # Append data to DataFrame and save as CSV
        df = df.append(data, ignore_index=True)
        df.to_csv("data.csv", index=False)

        # Clear the screen
        window.fill((0, 0, 0))

        # Display the data
        y = 0
        for sensor, readings in data.items():
            text = font.render(f"{sensor}: {readings}", True, (255, 255, 255))
            window.blit(text, (0, y))
            y += 40

        pygame.display.flip()

    except json.JSONDecodeError:
        pass  # in case the line is not valid JSON

'''
sensor["Wet Bulb Temperature C"] = temperature_wet;
    sensor["Partial Pressure of Water (bar) "] = partial_pressure_water;
    sensor["Mass Fraction of Water kg H20 /kg air mix"] = mass_frac_water;
    sensor["Mass Fraction of Air kg dry air / kg air mix"] = mass_frac_air;
    sensor["Air Enthalpy kJ / kg wet air"] = enthalpy;
    sensor["Partial Pressure of Water Vapor (bar)"] = partial_pressure_water_vapor;
    sensor["Wet Air Density kg/m³"] = wet_air_density;
    sensor["Dry Air Density kg/m³"] = dry_air_density;
    sensor["Air Density (dry temp) C"] = air_density;

    float temperature_wet = 20*atan(0.51977*sqrt((relative_humidity+8.313659))) + atan(temperature_dry + relative_humidity) -atan(relative_humidity - 1.676331) + 0.00391838*pow(sqrt(relative_humidity),3)*atan(0.023101*relative_humidity)-4.686035;
    float partial_pressure_water = exp(11.78*(temperature_wet-99.64)/(temperature_wet+230));
    float mass_frac_water = 0.62197*(partial_pressure_water/(1.01325-partial_pressure_water));
    float mass_frac_air = (1.0048*(temperature_wet-temperature_dry)+mass_frac_water*(2501-2.3237*temperature_wet))/(2501+1.86*temperature_dry-4.19*temperature_wet);
    float enthalpy = temperature_dry+mass_frac_air*(2501+1.86*temperature_dry);
    float partial_pressure_water_vapor = mass_frac_air*(1.01325/(mass_frac_air+0.62197));
    float wet_air_density =(((1.01325)*18*(mass_frac_air+1))/((0.083143*(273.15+temperature_dry)*(mass_frac_air+(18/28.97)))));
    float dry_air_density = wet_air_density*(1-mass_frac_air);
    float air_density = 1.293*273/(273+temperature_dry); 
'''
