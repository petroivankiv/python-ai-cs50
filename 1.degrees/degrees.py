import sys

from data_loader import load_data, people, names, movies
from util import Node, QueueFrontier


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "1.degrees/small"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    
    if source is None:
        sys.exit("Person not found.")
        
    target = person_id_for_name(input("Name: "))
    
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)
     
    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    root_neighbors: set = neighbors_for_person(source)
    root_nodes = set()
    
    for neighbor in root_neighbors:
        if neighbor[1] == source:
            root_nodes.add(neighbor)
            
    visited = set()
    
    for root in root_nodes:
        queue = QueueFrontier()
        queue.add(Node(root))
        visited.add(root)
       
        while queue.isNotEmpty():
            current = queue.remove()
            neighbors = neighbors_for_person(current.state[1])
            
            for neighbor in neighbors:
                node = Node(neighbor, current)
                
                if neighbor[1] == target:
                    return queue.getPath(node)
                
                if queue.contains_state(node) == False and neighbor not in visited:
                    visited.add(neighbor)
                    queue.add(node)
        
    return None
        


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
            
        try:
            person_id = input("Intended Person ID: ")
            
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
            
    return neighbors


if __name__ == "__main__":
    main()
