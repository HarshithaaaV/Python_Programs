#WAP tp ask the user to enter names of their 3 favourite movies & store them in a list

movies = []
for i in range(3):
    movies.append(input("Enter the name of your favourite movie: "))
print("Your favourite movies are: ", movies)