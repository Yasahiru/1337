# 🌱 ft_garden_analytics — Class & Method Specification

## Chapter XI – Exercise 6: Garden Analytics

This document describes **what each class must contain**, including its **attributes**, **methods**, and **responsibilities**.  
No implementation code is included — only *what you must do*.

---

## 1️⃣ Plant (Base Class)

### Attributes
1. `name`  
   - Stores the plant’s name

2. `height`  
   - Stores the current height of the plant (in cm)

### Methods
1. `grow()`  
   - Should increase the plant height by **1 cm**  
   - Should print a message indicating the plant has grown

2. `get_info()`  
   - Should return a basic textual description of the plant  
   - Used when generating garden reports

---

## 2️⃣ FloweringPlant (inherits from `Plant`)

### Attributes
1. `flower_color`  
   - Stores the flower color

2. `is_blooming`  
   - Boolean indicating whether the plant is blooming

### Methods
1. `grow()`  
   - Should call `super().grow()`  
   - Should set `is_blooming` to `True`  
   - Extends the base plant behavior

2. `get_info()`  
   - Should extend `Plant.get_info()`  
   - Should include flower color and blooming state

---

## 3️⃣ PrizeFlower (inherits from `FloweringPlant`)

### Attributes
1. `prize_points`  
   - Numeric value representing prize points

### Methods
1. `get_info()`  
   - Should extend `FloweringPlant.get_info()`  
   - Should include prize points information

---

## 4️⃣ Garden

### Attributes
1. `owner_name`  
   - Name of the garden owner

2. `plants`  
   - Collection (list) of plant objects

3. `stats`  
   - Instance of the statistics helper class

### Methods
1. `add_plant(plant)`  
   - Should add a plant to the garden  
   - Should update statistics  
   - Should print a confirmation message

2. `grow_all_plants()`  
   - Should call `grow()` on every plant in the garden  
   - Represents caring for all plants

3. `generate_report()`  
   - Should print:
     - All plant information  
     - Statistics summary

---

## 5️⃣ GardenManager

### Attributes
1. `gardens`  
   - Collection of all managed gardens

2. `total_gardens` *(class-level)*  
   - Tracks the total number of gardens created

### Instance Methods
1. `add_garden(garden)`  
   - Should register a garden in the manager  
   - Should update total garden count

2. `compare_gardens()`  
   - Should compare garden scores  
   - Should print comparison results

---

## 6️⃣ GardenManager.GardenStats (Nested Class)

### Attributes
1. `plants_added`  
   - Total number of plants added

2. `total_growth`  
   - Total growth in centimeters

3. `regular_count`  
   - Number of regular plants

4. `flowering_count`  
   - Number of flowering plants

5. `prize_count`  
   - Number of prize flowers

### Methods
1. `register_plant(plant)`  
   - Should detect plant type  
   - Should increment the correct counters

2. `register_growth()`  
   - Should increase total growth

3. `get_summary()`  
   - Should return all statistics in printable format

---

## 7️⃣ Class-Level Methods (GardenManager)

1. `create_garden_network()`  
   - Belongs to the **GardenManager class**, not instances  
   - Represents a system-wide setup  
   - Does not depend on specific garden data

2. `get_total_gardens()`  
   - Should return the number of gardens managed

---

## 8️⃣ Static / Utility Methods

1. `validate_plant_height(height)`  
   - Should validate a height value  
   - Returns `True` or `False`  
   - Does not depend on any object state

2. `calculate_garden_score(garden)`  
   - Should compute a garden score based on:
     - Plant heights  
     - Prize points  
   - Independent helper logic

---

## 9️⃣ Program Entry Point

1. `main()`  
   - Should demonstrate:
     - Creating the manager  
     - Creating gardens  
     - Adding plants  
     - Growing plants  
     - Printing reports

2. `if __name__ == "__main__":`  
   - Should call `main()`  
   - Ensures correct execution behavior

---

## 🧠 Recommended Implementation Order

1. Implement `Plant`, `FloweringPlant`, `PrizeFlower`
2. Implement `Garden`
3. Implement `GardenManager`
4. Add nested `GardenStats`
5. Add class and static methods
6. Write `main()` demonstration

---

## 🎯 Core Objective

This exercise tests your ability to:
- Design clean object-oriented systems
- Use inheritance and composition together
- Decide where behavior belongs (instance, class, or utility)
- Organize complex interacting components

Mastering this structure means mastering **real-world OOP design**.
