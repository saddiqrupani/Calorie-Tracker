from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt

CALORIE_GOAL = 2000
PROTEIN_GOAL = 175
FAT_GOAL = 78
CARB_GOAL = 150

today = []

@dataclass
class Food:
    name: str
    calories: int
    proteins: int
    fats: int
    carbs: int

done = False

while not done:
    print("""
    (1) Add calorie source
    (2) Visualize progress
    (q) Quit
    """)

    option = input("Choose an option: ")

    if option == "1":
        print("Adding a Calorie Source!")
        name = input("Name: ")
        calories = int(input("Calories: "))
        proteins = int(input("Proteins: "))
        fats = int(input("Fats: "))
        carbs = int(input("Carbs: "))
        food = Food(name, calories, proteins, fats, carbs)
        today.append(food)
        print("Successfully Added!")
    elif option == "2":
        calorie_sum = sum(food.calories for food in today)
        protein_sum = sum(food.proteins for food in today)
        fats_sum = sum(food.fats for food in today)
        carbs_sum = sum(food.carbs for food in today)

        fig, axs = plt.subplots(2, 2)
        axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels = ["Proteins", "Fats", "Carbs"], autopct = "%1.1f%%")
        axs[0, 0].set_title("Macronutrients Distribution")
        axs[0, 1].bar([0, 1, 2], [protein_sum, fats_sum, carbs_sum], width = 0.4)
        axs[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, FAT_GOAL, CARB_GOAL], width = 0.4)
        axs[0, 1].set_title("Macronutrients Progress")
        axs[1, 0].pie([calorie_sum, CALORIE_GOAL - calorie_sum], labels = ["Calories", "Remaining"], autopct = "%1.1f%%")
        axs[1, 0].set_title("Calorie Progress")
        axs[1, 1].plot(list(range(len(today))), np.cumsum([food.calories for food in today]), label = "Calories Eaten")
        axs[1, 1].plot(list(range(len(today))), [CALORIE_GOAL] * len(today), label = "Calorie Goal")
        axs[1, 1].legend()
        axs[1, 1].set_title("Calories Goal Over Time")
        fig.tight_layout()
        plt.show()
    elif option == "q":
        done = True
    else:
        print("Invalid Option!")
