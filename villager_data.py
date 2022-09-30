"""Functions to parse a file containing villager data."""
filename = "villagers.csv"


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    species = set()
    data = open(filename)
    for line in data:
        line = line.rstrip().split("|")
        species.add(line[1])
    
    return species

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    villagers = []
    data = open(filename)
    for line in data :
        line = line.rstrip().split("|")
        if line[1] == search_string:
            villagers.append(line[0])

    return sorted(villagers)

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.
education_list = ["claire", "jason", "beardo"]
list.append(education_list)
    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    data = open(filename)
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []
    
    for line in data: 
        data_line = line.rstrip().split("|")
       
        if data_line[3] == "Fitness":
            fitness.append(data_line[0])

        if data_line[3] == "Nature":
            nature.append(data_line[0])
        if data_line[3] == "Education":
            education.append(data_line[0])
        if data_line[3] == "Music":
            music.append(data_line[0])
        if data_line[3] == "Fashion":
            fashion.append(data_line[0])
        if data_line[3] == "Play":
            play.append(data_line[0])

    total_list = [fitness, nature, education, music, fashion, play]
    return total_list
    

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    data_list = []
    data = open(filename)
    for line in data: 
        data_line = line.rstrip().split("|")
        villagers = (data_line[0],data_line[1],data_line[2],data_line[3],
                    data_line[4])
        data_list.append(villagers)


    return data_list


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    data = open(filename)
    for line in data:
        data_line = line.rstrip().split("|")
        if data_line[0] == villager_name:
            answer = data_line[4]
    
    if answer != None:
        return answer
    else:
        return None


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
    villagers_with_same_personality = set()
    data_list=[]
    data = open(filename)
    for line in data:
        data_line = line.rstrip().split("|")
        data_list.append(data_line)
        if data_line[0] == villager_name:
            personality = data_line[2]
            print(personality)

    for data_line in data_list:
        if data_line[2] == personality: 
            villagers_with_same_personality.add(data_line[0])

    return villagers_with_same_personality

print(find_likeminded_villagers(filename, "Teddy"))