# Constants for formatting
titleWidth_row_1 = 55
titleWidth_row_2 = 35
starsWidth = 71

# Formatting for Movies with numerical alignment to help you out!!
#12345678901234567890123456789012345678901234567890123456789012345678901234567890
#Title                                                    |  X h YY min  |  PG-13
#Title part 2                         |  Director: John Smith
#Title part 3                         |  Writer:   John Jacob Jingleheimer Schmit
#Genre:   Comedy|Drama|Romance|Fantasy
#Stars:   John Jacob Jingleheimer Schmidt, Jane Jacob Jingleheimer Schmidt,
#         Joanna Killington
#Release: May 24, 2008

class Movie(object):
    """Stores the data for a single Movie"""
    def __init__(self, title, genre, director, writer, star1, star2, star3, time1, rating, release):
        # TODO: Initialize the Movie object
        self.__title=title
        self.__genre=genre
        self.__director=director
        self.__writer=writer
        self.__star1=star1
        self.__star2=star2
        self.__star3=star3
        self.__time=time1
        self.__rating=rating
        self.__release=release
        pass

    def __str__(self):
        ''' Return the movie as a string '''
        # TODO: return a string version of the Movie object - this is what will be called by print!
        hours=int(self.__time)/60
        minutes=int(self.__time)%60
        title1=str(self.__title)[0:54]
        title2=str(self.__title)[55:90]
        title3=str(self.__title)[91:]
        
        
        
        print("-" * 80)

        return ("{:55}  |  {:1f} h {:.2f} m  |  {:>}\n{:35} |  Director: {:10}\n{:35} |  Writer:   {:10}\nGenre:   {:71}\nStars:   \nRelease: {:30}".format(title1, hours, minutes, self.__rating, title2, self.__director, title3, self.__writer, self.__genre, self.__release))
        pass

    def getTitle(self):
        ''' Return the movie title '''
        # TODO: return the title of the Movie
        return self.__title
        pass

    def getGenre(self):
        ''' Return the movie genre '''
        # TODO: return the genre of the Movie
        return self.__genre
        pass

    def getDirector(self):
        ''' Return the movie director '''
        # TODO: return the director of the Movie
        return self.__director
        pass

    def getWriter(self):
        ''' Return the movie writer '''
        # TODO: return the writer of the Movie
        return self.__writer
        pass

    def getStars(self):
        ''' Return the movie stars '''
        # TODO: return the stars of the Movie
        return self.__star1, self.__star2, self.__star3
        pass

    def getTime(self):
        ''' Return the movie time '''
        # TODO: return the time of the Movie
        return self.__time
        pass

    def getRating(self):
        ''' Return the movie rating '''
        # TODO: return the rating of the Movie
        return self.__rating
        pass

    def getRelease(self):
        ''' Return the movie release year '''
        # TODO: return the release year of the Movie
        return self.__release
        pass

