class Person:
    def __init__(self, name):
        self.name = name
        self.connections = []  # List of connected cities
    
    def add_connection(self, other_person):
    # Connect this person to another person
        if other_person not in self.connections:
            self.connections.append(other_person)

# Create individual people 
dennis = Person("Dennis")
sally = Person("Sally")

print(dennis.name)  # Dennis
dennis.add_connection(sally)
print(dennis.connections[0].name)  # Sally
'''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    



class SocialNetwork:
    
  def __init__(self):
    self.people = {}  # Dictionary: people_name -> people object
    
  def add_person(self, name):
    """Add a new person to the network"""
    if name not in self.people:
      self.people[name] = Person(name)
    
  def add_friendship(self, person1_name, person2_name):
    """Add a bidirectional frienship between two people"""
    if person1_name in self.people and person2_name in self.people:
      person1 = self.people[person1_name]
      person2 = self.people[person2_name]
                  
      # Create bidirectional connection
      person1.add_connection(person2)
      person2.add_connection(person1)
    else:
      print(f"Error: One or both pepople don't exist!")


  def print_SocialNetwork(self): 
    for person_name, person_obj in self.people.items(): 
      # List of connected people names 
        connection_names = [c.name for c in person_obj.connections]
      
      # Join names with a comma
    connected_people = ", ".join(connection_names)
    print(f"{person_name} connects to: {connected_people}")
       



# Build the network
network = SocialNetwork()
network.add_person("Lilly") 
network.add_person("Luke") 
network.add_person("Jakob") 
network.add_friendship("Lilly", "Luke") 
network.add_friendship("Lilly", "Jakob") 
# Returns dictionary that points to each people associated object 
print(network.people) # {'Lilly': <__main__.person object at 0x1004cb380>, 'Luke': <__main__.person object at 0x1005fd6d0>, 'jakob': <__main__.City object at 0x1005fd810>} 
print(network.people["Lilly"].connections[0].name)  # "Luke"
network.print_SocialNetwork()
'''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
'''
    
   



# Test your code here

# Build a network of 6 people
network = SocialNetwork()
for name in ["Lilly", "Luke", "Jakob", "Maya", "Noah", "Zoe"]:
    network.add_person(name)

# 8 friendships
network.add_friendship("Lilly", "Luke")
network.add_friendship("Lilly", "Jakob")
network.add_friendship("Lilly", "Maya")
network.add_friendship("Luke", "Jakob")
network.add_friendship("Luke", "Noah")
network.add_friendship("Jakob", "Zoe")
network.add_friendship("Maya", "Noah")
network.add_friendship("Noah", "Zoe")

# Edge case 1: friendship with a person who doesn't exist
network.add_friendship("Lilly", "Nobody")      # should print an error

# Edge case 2: adding a duplicate person
network.add_person("Lilly")
print(len(network.people))                     # should still be 6

# Edge case 3: duplicate friendship
network.add_friendship("Lilly", "Luke")
print(len(network.people["Lilly"].connections))  # should still be 3

# Print the whole network
network.print_SocialNetwork()