import explorerhat as eh
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

#Be sure to add your experimental voltage values between the brackets separated by a ‘,’
voltages = [ ]  #This is a list of voltages
pH_values = [10.0, 7.0, 4.0]  #This is a list of corresponding pH values.  Note their order!

graph = False  # create a variable to hold a state flag

while True:
	voltage = round(eh.analog.one.read(), 2)
	print(f”The voltage is {voltage} V. Press pad 1 when stabilized.”)
	sleep(1)
	if eh.touch.one.is_pressed():
		graph = True
		print(f”The voltage {voltage} is being converted into a pH reading.”)
	if graph == True:
		graph = False # Lower the state flag
	#create a line graph from your experimental data
	plt.plot(voltages, pH_values, ‘bo-’) #blue dots connected with a line
	plt.xlabel(‘voltage (V)’)
	plt.ylabel(‘pH’)
	plt.title(‘Analog Voltage to pH Conversion’)

	#Interpolate your data to estimate the pH of your sensor to the nearest tenth
	pH = round(np.interp(voltage, voltages, pH_values),1)

	plt.plot(voltage, pH, ‘r^’) # plots the pH as a red triangle
	plt.annotate(str(pH), xy= (reading, pH + 0.25)) # labels the interpolated mark

	plt.show() # Displays the graph on the screen for visualization
