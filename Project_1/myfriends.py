
"""Assignment 1: Friend of a Friend


Please complete these functions, to answer queries given a dataset of
friendship relations, that meet the specifications of the handout
and docstrings below.

Notes:
- you should create and test your own scenarios to fully test your functions, 
  including testing of "edge cases"
"""

from friends import Friends

"""
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************

If you worked in a group on this project, please type the EIDs of your groupmates below (do not include yourself).
Leave it as TODO otherwise.
Groupmate 1: ss66248
Groupmate 2: cwp764
"""

def load_pairs(filename):
    """
    Args:
        filename (str): name of input file

    Returns:
        List of pairs, where each pair is a Tuple of two strings

    Notes:
    - Each non-empty line in the input file contains two strings, that
      are separated by one or more space characters.
    - You should remove whitespace characters, and skip over empty input lines.
    """
    list_of_pairs = []
    with open(filename, 'rt') as infile:
        for pairs in infile:
            x = pairs.split()
            v1 = x[0]
            v2 = x[1]
            my_tupple = (v1, v2)
            list_of_pairs.append(my_tupple)

        return list_of_pairs


def make_friends_directory(my_pairs):
    """Create a directory of persons, for looking up immediate friends

    Args:
        pairs (List[Tuple[str, str]]): list of pairs

    Returns:
        Dict[str, Set] where each key is a person, with value being the set of 
        related persons given in the input list of pairs

    Notes:
    - you should infer from the input that relationships are two-way: 
      if given a pair (x,y), then assume that y is a friend of x, and x is 
      a friend of y
    - no own-relationships: ignore pairs of the form (x, x)
    """
    directory = dict()



    # ------------ BEGIN YOUR CODE ------------

    my_pairs_copy = []

    # Create a list of tuples (y,x) from a list of tuples (x,y)
    my_pairs_copy = my_pairs[:]   # copy of the list (x,y)
    #print(my_pairs_copy)

    # Swapping (x, y) to (y, x)
    my_pairs_swapped_tuples = [(sub[1], sub[0])  for sub in my_pairs_copy]
   # print(my_pairs_swapped_tuples)

    # create a list that contains both (x,y) and (y,x)
    my_pairs_large_list = my_pairs + my_pairs_swapped_tuples
    #print(my_pairs_large_list)
    #print(len(my_pairs))
    #print(len(my_pairs_large_list))

    # Create a set of all the names  and put them in alphabetical order
    my_pairs_first_element_of_tupple = [x[0] for x in my_pairs_large_list]
    #print(my_pairs_first_element_of_tupple)

    my_pairs_set = {*my_pairs_first_element_of_tupple}  # create a set from a list
    #print(my_pairs_set)

    sorted_my_pairs_set = sorted(my_pairs_set)
   # print(sorted_my_pairs_set)

    sorted_my_pairs_large_list = sorted(my_pairs_large_list)
    #print(sorted_my_pairs_large_list)

    for i in sorted_my_pairs_set:
        my_tuple = ()
        my_list_i= []
        my_list_j = []
        for j in sorted_my_pairs_large_list:
            if i == j[0]:
                 my_list_j.append( j[1])
                 #print(my_list_i)
        my_set = set(my_list_j)
        #print(my_tuple)
        directory[i] = my_set
    # ------------ END YOUR CODE ------------

    return directory


def find_all_number_of_friends(my_dir):
    """List every person in the directory by the number of friends each has

    Returns a sorted (in decreasing order by number of friends) list 
    of 2-tuples, where each tuples has the person's name as the first element,
    the the number of friends as the second element.
    """
    friends_list = []

    # ------------ BEGIN YOUR CODE ------------

    for x in my_dir:
        # my_key = k
        # my_length_of_value = str(len(my_dir[k]))
        # my_tuple = ( my_key, my_length_of_value)
        # friends_list.append(my_tuple)
        friends_list += [(x, len(my_dir[x]))]

    friends_list = sorted(friends_list)
    friends_list.sort(key = lambda x: x[1], reverse = True)

    # ------------ END YOUR CODE ------------

    return friends_list


def make_team_roster(person, my_dir):
    """Returns str encoding of a person's team of friends of friends
    Args:
        person (str): the team leader's name
        my_dir (Dict): dictionary of all relationships

    Returns:
        str of the form 'A_B_D_G' where the underscore '_' is the
        separator character, and the first substring is the 
        team leader's name, i.e. A.  Subsequent unique substrings are 
        friends of A or friends of friends of A, in ascii order
        and excluding the team leader's name (i.e. A only appears
        as the first substring)

    Notes:
    - Team is drawn from only within two circles of A -- friends of A, plus 
      their immediate friends only
    """
    assert person in my_dir
    label = person


    # ------------ BEGIN YOUR CODE ------------
    my_list = [label]
    my_list2 = []
    friends_tuple = (my_dir[label])
    friends_list = list(friends_tuple)

    # Create a list of the friends of the leader

    for item in friends_list:
        my_list.append(item)
    #print(my_list)

    # Create a list of the friends of the friends of the captain
    for x in my_list:
        friends_of_friends_tuple = (my_dir[x])
        friends_of_friends_list = list(friends_of_friends_tuple)
        #print( friends_of_friends_list)

        for y in friends_of_friends_list:
            my_list2.append(y)
    #print('my list2',my_list2)

    total_list = my_list + my_list2         # Combine the friends and the friends of the friends of the captain
    # print('tot list',total_list)
    # print(len(my_list))
    # print(len(my_list2))
    # print(len(total_list))

    unduplicated_list = list(set(total_list)) # remove duplicate names from list
    #print('undup',unduplicated_list)

    unduplicated_list.sort()                  # sort list
    #print(unduplicated_list)

    unduplicated_list.remove(label)             # remove team captains name from the list
    #print(unduplicated_list)


    # Convert list to a string with a '_' between names
    team_roster = label      # put team captain to the front of the string
    for name in unduplicated_list:
        team_roster = team_roster + '_' + name
    #print('tr', team_roster)



    # ------------ END YOUR CODE ------------

    return team_roster


def find_smallest_team(my_dir):
    """Find team with smallest size, and return its roster label str
    - if ties, return the team roster label that is first in ascii order
    """
    all_teams = []
    smallest_teams = []

    # ------------ BEGIN YOUR CODE


    # for key in my_dir:
    #     team_roster = make_team_roster(key, my_dir)         # call method make_team_roster
    #     #print('st', team_roster)
    #
    #     new_team_roster_string = team_roster.replace("_", ", ")   # replace "_" with , and a space
    #    # print(new_team_roster_string)
    #
    #     string_to_tuple = tuple(map(str, new_team_roster_string.split(', ')))
    #     #print(string_to_tuple)
    #
    #     length_of_string = len(string_to_tuple) -1         # length of the string minus the team leader
    #     #print(length_of_string)
    #
    #     team_leader = string_to_tuple[0]
    #     #print(team_leader)
    #
    #     leader_team_tuple = (team_leader, length_of_string)
    #     #print(leader_team_tuple)
    #
    #     all_teams.append(leader_team_tuple)
    #     #print(all_teams)
    #
    # all_teams.sort(key=lambda x: x[1])              # sort by team size in ascending order
    #     #print(all_teams)
    #
    # smallest_team_size = all_teams[0][1]
    # #print(smallest_team_size)
    #
    # # Compare team size with the smallest size and if it is equal in size then add to list
    # for item in all_teams:
    #     if item[1] == smallest_team_size:
    #         smallest_teams.append(item)
    # #print(smallest_teams)
    # smallest_teams.sort(key=lambda x: x[1])

    for x in my_dir:
        team = make_team_roster(x, my_dir)
        teamLength = len(team.split("_"))
        smallest_teams += [(team, teamLength)]
    smallest_teams = sorted(smallest_teams)
    smallest_teams.sort(key=lambda dirEntry: dirEntry[1])
    for x in range(len(smallest_teams)):
        smallest_teams[x] = smallest_teams[x][0]
    # ------------ END YOUR CODE

    return smallest_teams[0] if smallest_teams else ""


    
    # ------------ END YOUR CODE

    return smallest_teams[0][0] if smallest_teams else ""



if __name__ == '__main__':
    # To run and examine your function calls

    print('\n1. run load_pairs')
    my_pairs = load_pairs('myfriends.txt')
    print(my_pairs)

    print('\n2. run make_directory')
    my_dir = make_friends_directory(my_pairs)
    print(my_dir) 

    print('\n3. run find_all_number_of_friends')
    print(find_all_number_of_friends(my_dir))

    print('\n4. run make_team_roster')
    my_person = 'BIGGS'   # test with this person as team leader
    team_roster = make_team_roster(my_person, my_dir)
    print(team_roster) 

    print('\n5. run find_smallest_team')
    print(find_smallest_team(my_dir))

    print('\n6. run Friends iterator')
    friends_iterator = Friends(my_dir)
    for num, pair in enumerate(friends_iterator):
        print(num, pair)
        if num == 10:
            break
    print(len(list(friends_iterator)) + num)
