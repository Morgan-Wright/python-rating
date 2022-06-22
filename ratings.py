print("Welcome to the restaurant rating lister.")

movies = {"Florean Fortescue's Ice Cream Parlour": '4',
          "Jellied Eel Shop": '3',
          "The Tavern": '3',
          "Luchino Caffe": '1',
          "The Porcupine": '5',
          "Diagon Alley cafe": '2',
          "The Bear & Staff": '2',
          "Ministry Munchies": '1',
          "Chip Shop": '3',
          "Eternelle's Elixir of Refreshment": '5',
          "Big Bean Shack": '3',
          "The Club": '2'
          }

def sorted_list(movies):
    for key, value in sorted(movies.items()):
        print(key, value)

sorted_list(movies)   
restaurant = input("Please select a restaurant from the list.\n")
rating = input(f"Please give {restaurant} a star rating out of 5.\n")

# movies.update(restaurant = rating)

if restaurant in movies.keys():
    movies.update()

print(sorted_list(movies))
