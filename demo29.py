# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Flirida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
    }
    
# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
    }
    
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print ('-' * 10)
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])

# print some states
print ('-' * 10)
print ("Michigan's abbreviation is:", states['Michigan'])
print ("Florida's abbreviation is:", states['Flirida'])

# do it bu suing the state then cities dict
print ('-' * 10)
print ("Michigan has: ", cities[states['Michigan']])
print ("Florida has: ", cities[states['Flirida']])

# print every state abbreviation
print ("-" * 10)
# 这里的states.items()代表了字典里的每一个词条，states以及abbrev分别接收词目和词条内容
for state, abbrev in states.items():
    print ("{:s} is abbreviated {:s}".format(state, abbrev))

# print every city in state
print ('-' * 10)
for abbrev, city in cities.items():
    print ("{:s} has the city {:s}".format(abbrev, city))
    
# now do both at the same time
print ('-' * 10)
for state, abbrev in states.items():
    print("{:s} state is abbreviated {:s} and has city {:s}".format(state, abbrev, cities[abbrev]))
    
print ('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Taxas', False)
# get方法的第一个参数为需要获取的词目，若无，则返回第二个参数的内容
print (state)

if not state:
        print ("Sorry, no Texas.")
        
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print ("The city for the state 'TX' is :{:s}".format(city))