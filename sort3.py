# Take number of cities
n = int(input("Enter the number of cities: "))

cities = []

# Take city names and distances from user
for i in range(n):
    name = input("Enter name of city " + str(i + 1) + ": ")
    distance = int(input("Enter distance for " + name + ": "))
    cities.append((name, distance))

while True:
    # Ask user how they want to sort
    print("\nHow do you want to sort?")
    print("1. Sort by Distance")
    print("2. Sort by City Name")
    print("3. Exit")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 3:
        print("Exiting...")
        break

    elif choice in [1, 2]:
        # Greedy Selection Sort
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if choice == 1:
                    if cities[j][1] < cities[min_idx][1]:
                        min_idx = j
                elif choice == 2:
                    if cities[j][0] < cities[min_idx][0]:
                        min_idx = j
            # Swap
            cities[i], cities[min_idx] = cities[min_idx], cities[i]

        # Print the sorted list
        print("\nCities after sorting:")
        for city, distance in cities:
            print(city + " - " + str(distance))
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
