import re
import Movie
from Movie import *

###########################################################################
# Functions
###########################################################################

def printMenu(menuItems):
	''' Print the menu to the user '''
	menuItem = 0

	# Print a horizontal line of asterisks
	print("*" * 30)

	# For each menu item, print it neatly formatted with its message
	for item in menuItems:
		menuItem += 1
		print("%d - %s" % (menuItem, item))

	# Print a horizontal line of asterisks
	print("*" * 30)

	# Ask the user for their response and return it
	return promptForInteger(1, menuItem, 
						    "Please make a selection between 1 and %d:" % menuItem, 
							"Your response must be number between 1 and %d, try again." % menuItem)

def promptForInteger(minimum, maximum, message, errorMessage):
	''' Prompt for an integer from the user and validate it within
	    the provided range '''

	# Try to read an integer from the user, if they input anything other than
	# a valid integer, assume it was an error
	try:
		response = int(input(message + "\n"))
	except:
		response = -1

	# Until they provide a valid value, reprompt
	while (response < minimum or response > maximum):
		try:
			response = int(input(errorMessage + "\n"))
		except:
			response = -1
	return response

def parseMovie(line, movies):
	''' Parse individual movie data from the provided line and append it to the list '''
	entries = []

	# Remove the return at the end of the line
	line = line.strip('\n')

	# If the title starts with a double-quote, take it off first as it has a
	# comma in the movie title itself
	if line.startswith('"'):
		match = re.search('".+"', line)
		entries.append(match.group(0).strip('"'))
		line = line[len(entries[0]) + 3:]

	# Split the rest of the content based on commas
	entries += line.split(",")

	# If there are the right number of components in the movie data, create a movie
	if len(entries) == 10:
		movies.append(Movie(entries[0], entries[1], entries[2], entries[3], entries[4], \
							entries[5], entries[6], entries[7], entries[8], entries[9]))

def loadFile(message, movies):
	''' Load the movies from the user provided file '''
	# Ask the user for the filename
	filename = input(message + "\n")

	# Open the file in read mode
	file = open(filename, "r")

	# If the file was opened
	if file.mode == 'r':

		# Read all of the lines from the file
		contents = file.readlines()

		# Skip the first line as it is the header line, 
		# parse movies from the remaining lines
		for line in contents[1:]:
			parseMovie(line, movies)

	# If the file could not be opened, display an error
	else:
		print("File could not be found: " + filename)

def searchByTitle(message, movies):
  criteria = input(message + "\n")
	# TODO: search the movies by title where criteria is the user's search term
  pattern=str(criteria)
  
  for i in range(len(movies)):
    if re.search(str(pattern),movies[i].getTitle(), re.IGNORECASE):
      print(movies[i].__str__())
  
def searchByGenre(message, movies):
  criteria = input(message + "\n")
	# TODO: search the movies by genre where criteria is the user's search term
  pattern=str(criteria)
  
  for i in range(len(movies)):
    if re.search(str(pattern),movies[i].getGenre(), re.IGNORECASE):
      print(movies[i].__str__())

def searchByDirector(message, movies):
  criteria = input(message + "\n")
	# TODO: search the movies by director where criteria is the user's search term
  pattern=str(criteria)
  for i in range(len(movies)):
     if re.search(str(pattern),movies[i].getDirector(), re.IGNORECASE):
       print(movies[i].__str__())

def searchByWriter(message, movies):
  criteria = input(message + "\n")
	# TODO: search the movies by writer where criteria is the user's search term
  pattern=str(criteria)
  for i in range(len(movies)):
     if re.search(str(pattern),movies[i].getWriter(), re.IGNORECASE):
       print(movies[i].__str__())

def searchByStar(message, movies):
	''' Search the movie collection by star and find all matches '''
	criteria = input(message + "\n")
	# TODO: search the movies by star where criteria is the user's search term

def searchByRunningTime(message, movies):
	''' Search the movie collection by running time and find all matches '''
	criteria = input(message + "\n")
	# TODO: search the movies by running time where criteria is the user's search term

def searchByRating(message, movies):
	''' Search the movie collection by rating and find all matches '''
	criteria = input(message + "\n")
	# TODO: search the movies by rating where criteria is the user's search term

def searchByReleaseYear(message, movies):
	''' Search the movie collection by release year and find all matches '''
	criteria = input(message + "\n")
	# TODO: search the movies by release year where criteria is the user's search term

def printMovies(movies):
	''' Print all of the movies in sorted order by title '''
	# TODO: sort the movies and then print them in order
 
  #print("-" * 80)
  #      print("{:15}  |  {:1f} h {:.2f} m  |  {:>}".format(self.__title, hours, minutes, self.__rating))
        
	pass

###########################################################################
# Main
###########################################################################
movies = [ ]
movieList=[]
response = 0

# Until the user elects to quit the application, present the menu and
# process the user's selections
while response != 11:
	response = printMenu( [ "Load a Movie File", "Search by Title", "Search by Genre", "Search by Director", \
							"Search by Writer", "Search by Star", "Search by Running Time", \
							"Search by Rating", "Search by Release Year", "Print all Movies", "Quit" ] )

	if response == 1:
		movies = [ ]
		loadFile("Please enter the movie filename: ", movies)
	elif response == 2:
		searchByTitle("Please enter the movie title or partial title: ", movies)
	elif response == 3:
		searchByGenre("Please enter the movie genre or partial genre: ", movies)
	elif response == 4:
		searchByDirector("Please enter the Director's name or partial name: ", movies)
	elif response == 5:
		searchByWriter("Please enter the Writer's name or partial name: ", movies)
	elif response == 6:
		searchByStar("Please enter the Star's name or partial name: ", movies)
	elif response == 7:
		searchByRunningTime("Please enter the maximum running time in minutes: ", movies)
	elif response == 8:
		searchByRating("Please enter the movie rating: ", movies)
	elif response == 9:
		searchByReleaseYear("Please enter the release year: ", movies)
	elif response == 10:
		printMovies(movies)
	elif response == 11:
		print("Quitting!")
		exit