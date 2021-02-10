# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def cleanDamage(lst):
  result = []
  for data in lst:
    if data == 'Damages not recorded':
      result.append('Damages not recorded')
    elif 'M' in data:
      new_i = float(data.replace('M', '')) * 1000000
      result.append(new_i)
    elif 'B' in data:
      new_i = float(data.replace('B', '')) * 1000000000
      result.append(new_i)
  return result
updated_damage = cleanDamage(damages)
#print(updated_damage) 

# 2 
# Create and view the hurricanes dictionary
def hurricaneDict(names, months, years, max_sustained_winds, areas_affected, damage, deaths):
  result = {}
  hurr_len = len(names)
  for i in range(hurr_len):
    result[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': damage[i], 'Deaths': deaths[i] }
  return result
hurricane_dict = hurricaneDict(names, months, years, max_sustained_winds, areas_affected, updated_damage, deaths)
#print(hurricane_dict)
# 3
# Organizing by Year
def hurricane_year(dict):
  new_dict ={}
  for element in dict:
    current_year = dict[element]['Year']
    current_cane = dict[element]
    #print(current_year, current_cane)
    if current_year in new_dict:
      new_dict[current_year].append(current_cane)
    else:
      new_dict[current_year] = [current_cane]
  return new_dict
# create a new dictionary of hurricanes with year and key
hurricane_by_year = hurricane_year(hurricane_dict)

# 4
# Counting Damaged Areas
def area_affected_count(lst):
  result = {}
  for key in lst:
    #print(len(lst[key]['Areas Affected']))
    for i in range(len(lst[key]['Areas Affected'])):
      city = lst[key]['Areas Affected'][i]
      #print(lst[key]['Areas Affected'][i])
      if city in result:
        result[city] += 1
      else:
        result[city] = 1
  return result       
# create dictionary of areas to store the number of hurricanes involved in
area_damage_count = area_affected_count(hurricane_dict)
#print(area_damage_count)

# 5 
# Calculating Maximum Hurricane Count
def most_area_affected(lst):
  max_area = ''
  max_area_count = 0
  for area in lst:
    if lst[area] > max_area_count:
      max_area = area
      max_area_count = lst[area]
    #print(lst[area])
  return max_area, max_area_count    
#print(most_area_affected(area_damage_count))

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(dic):
  max_mortality = ''
  max_mortality_count = 0
  for hurricane in dic:
    if dic[hurricane]['Deaths'] > max_mortality_count:
      max_mortality = dic[hurricane]['Name']
      max_mortality_count = dic[hurricane]['Deaths']
  return max_mortality, max_mortality_count
# find highest mortality hurricane and the number of deaths
#print(deadliest_hurricane(hurricane_dict))

# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
def hurricane_mortality_rate(dic):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in dic:
    death = dic[hurricane]['Deaths']
    if death < 0:
      hurricanes_by_mortality[0].append(dic[hurricane])
    elif death >= 0 and death < 100:
      hurricanes_by_mortality[1].append(dic[hurricane])
    elif death >= 100 and death < 500:
      hurricanes_by_mortality[2].append(dic[hurricane])
    elif death >= 500 and death < 1000:
      hurricanes_by_mortality[3].append(dic[hurricane])
    elif death >= 1000 and death < 10000:
      hurricanes_by_mortality[4].append(dic[hurricane])
    else:
      hurricanes_by_mortality[5].append(dic[hurricane])    
  return hurricanes_by_mortality         
#print(hurricane_mortality_rate(hurricane_dict))  

# 8 Calculating Hurricane Maximum Damage
def hurricane_greatest_damage(dic):
  greatest_damage = ''
  damage = 0
  for hurricane in dic:
    if dic[hurricane]['Damage'] == 'Damages not recorded':
      continue
    if dic[hurricane]['Damage'] > damage:
      greatest_damage = hurricane
      damage = dic[hurricane]['Damage']
  return greatest_damage,damage   
# find highest damage inducing hurricane and its total cost
#print(hurricane_greatest_damage(hurricane_dict))

# 9
# Rating Hurricanes by Damage
def hurricane_damage_rate(dic):
  damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in dic:
    damage = dic[hurricane]['Damage']
    if dic[hurricane]['Damage'] == 'Damages not recorded':
      continue
    if damage < damage_scale[0]:
      hurricanes_by_damage[0].append(dic[hurricane])
    elif damage > damage_scale[0] and damage < damage_scale[1]:
      hurricanes_by_damage[1].append(dic[hurricane])
    elif damage >= damage_scale[1] and damage < damage_scale[2]:
      hurricanes_by_damage[2].append(dic[hurricane])
    elif damage >= damage_scale[2] and damage < damage_scale[3]:
      hurricanes_by_damage[3].append(dic[hurricane])
    elif damage >= damage_scale[3] and damage < damage_scale[4]:
      hurricanes_by_damage[4].append(dic[hurricane])
    else:
      hurricanes_by_damage[5].append(dic[hurricane])    
  return hurricanes_by_damage       
# categorize hurricanes in new dictionary with damage severity as key
#print(hurricane_damage_rate(hurricane_dict))