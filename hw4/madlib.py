story = "{0} was {1} by a bus. {0} felt {2}. So, {0} decided to {3} that bus. And {0} {1} that bus about half of hour. And {0} remeber that he has a meeting with {4} ."
name = raw_input("enter a man's name")
verb = raw_input("enter a verb")
adjective = raw_input("enter a adjective")
verb2 = raw_input("enter a verb2")
name2 = raw_input("enter a woman's  name2")

adjusted = story.format(name, verb, name, adjective, )
adjusted = name + " was " + verb + " by a bus. " + name + " felt " + adjective + "." + " So, " + name + " decided to " + verb2 + " bus. And " + name + verb + " that bus about half of hour. And " + name +
 " remeber that he has a meeting with " + name2 + "."



story
print(adjusted)
