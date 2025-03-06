#!/usr/bin/env python3
"""
bandNameGenerator.py - A simple script to generate a band name.

Author: Carlos Valerio
Date: 2025-03-06
License: NA
Dependencies: None (built-in functions only)

Description:
This script generates a band name by combining the name of the city the user grew up in
with the name of their pet. It simply asks for user input, concatenates the two,
and displays the generated band name.

Usage:
Run the script and follow the prompts:
    python bandNameGenerator.py

Example Output:
    Welcome to the Band Name Generator!
    Enter the city you grew up in: Seattle
    Enter the name of your pet: Shadow
    Your band name could be: Shadow Seattle
"""

#Welcome title
print("Welcome to the band name generator!")

#User input, City user grew in
bandName = input("Which city did you grow in: ")

#Second User input, Name of their pet
#Concatenates name of the city and the pet's name
bandName = bandName + " "+ input("What's the name of your pet: ")

#Shows the result
print(f"Your band name could be {bandName}")