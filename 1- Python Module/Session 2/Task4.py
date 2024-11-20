# Write a python code that generate an initialization function for DDRA register in atmega32
# microcontroller . the system will ask user to enter the mode for each pin, then generate a function called:
# void DDRA_init(void)-> that do the code .

import DDRA_Pack
import DDRA_Pack.DDRA

DDRA_Pack.DDRA.DDRA_Fun()
print("This is Atmega32")