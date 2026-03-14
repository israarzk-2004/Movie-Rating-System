# Movie-Rating-System

## Overview

The Movie Rating System is a simple Python program that helps users manage and rate movies.
The system allows the user to add movies, display all stored movies, search for a specific movie, delete movies, and identify the highest-rated movie.

This project demonstrates basic programming concepts in Python such as object-oriented programming, lists, loops, conditions, and functions.

---

## Features

* Add a movie with its rating.
* Display all movies stored in the system.
* Search for a movie by its name.
* Delete a movie from the list.
* Show the best movie based on the highest rating.

---

## How the System Works

The program runs through a menu displayed to the user.
The user selects an option from the menu, and the program performs the corresponding action.

Menu options include:

1. Add Movie
2. Show All Movies
3. Search Movie
4. Delete Movie
5. Show Best Movie
6. Exit

The program continues running until the user chooses the Exit option.

---

## Program Structure

### Movie Class

The program uses a class called **Movie** to represent each movie.
Each movie has:

* a name
* a rating

The class also contains methods to determine the category of the movie based on its rating and to display the movie information.

### Movie List

All movies are stored in a list called **movies**.
Each element in this list is an object created from the Movie class.

### Functions

Several functions are used to organize the program:

* **add_movie()** → adds a new movie to the list
* **show_all_movies()** → displays all movies in the system
* **find_movie()** → searches for a movie by name
* **delete_movie()** → removes a movie from the list
* **show_best_movie()** → finds and displays the movie with the highest rating

The best movie is determined using the Python `max()` function with a lambda expression.

---

## Learning Outcomes

This project helps in understanding:

* Object-Oriented Programming (OOP)
* Using lists to store objects
* Writing and using functions
* Conditional statements
* Loop structures
* Lambda expressions

---

## Conclusion

The Movie Rating System is a small project designed to practice basic Python programming concepts.
It provides a simple way to manage and evaluate movies while applying fundamental programming techniques.
