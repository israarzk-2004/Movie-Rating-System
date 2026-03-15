#Movie Rating System
# Uses: Variables - Lists - Loops - Conditions - Functions - OOP

class Movie:
def __init__(self, name, rating):  
    self.name = name
    self.rating = rating

    def get_category(self):
        if self.rating < 7:
            return "Bad"
        elif self.rating > 8.5:
            return "Great"
        else:
            return "Good"

    def show_info(self):
        print("\n--- Movie Info ---")
        print("Name:", self.name)
        print("Rating:", self.rating)
        print("Category:", self.get_category())
        print("-------------------")



movies = []


def add_movie():
    print("\nAdd New Movie")
    name = input("Enter movie name: ")
    rating = float(input("Enter rating (0-10): "))

    movie = Movie(name, rating)
    movies.append(movie)

    print(f"\nMovie {name} added successfully!")


def show_all_movies():
    if len(movies) == 0:
        print("\nNo movies found.")
        return

    print("\n=== All Movies ===")
    for m in movies:
        m.show_info()


def find_movie():
    name = input("\nEnter movie name to search: ")

    found = False
    for m in movies:
        if m.name.lower() == name.lower():
            m.show_info()
            found = True
            break

    if not found:
        print(f"\nMovie '{name}' not found.")


def delete_movie():
    name = input("\nEnter movie name to delete: ")

    for m in movies:
        if m.name.lower() == name.lower():
            movies.remove(m)
            print(f"\nMovie '{name}' deleted successfully!")
            return

    print(f"\nMovie '{name}' not found.")
    
# Lambda Example (Best Movie)
def show_best_movie():
    if not movies:
        print("\nNo movies available.")
        return

    best_movie = max(movies, key=lambda m: m.rating)
    print("\nBest Movie:")
    best_movie.show_info()


# Main Menu
def main():
    while True:
        print("\n===== Movie Rating System =====")
        print("1. Add Movie")
        print("2. Show All Movies")
        print("3. Search Movie")
        print("4. Delete Movie")
        print("5. Show Best Movie")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_movie()

        elif choice == "2":
            show_all_movies()

        elif choice == "3":
            find_movie()

        elif choice == "4":
            delete_movie()

        elif choice == "5":
            show_best_movie()

        elif choice == "6":
            print("\nExiting... Goodbye!")
            break

        else:
            print("\nInvalid choice. Try again.")


main()
