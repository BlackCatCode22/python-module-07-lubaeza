from Animal import Animal
from Tiger import Tiger
from Lion import Lion
from Hyena import Hyena
from Bear import Bear

from _datetime import date

list_of_lions = []
list_of_tigers = []
list_of_hyenas = []
list_of_bears = []

current_date = date.today()
current_year = current_date.year

def calc_birth_date(the_season, the_years):
  year_of_birthday = int(current_year) - int(the_years)

  the_birth_day = ""

  if "spring" in the_season:
    the_birth_day = str(year_of_birthday) + "-03-21"
  elif "summer" in the_season:
    the_birth_day = str(year_of_birthday) + "-06-21"
  elif "fall" in the_season:
    the_birth_day = str(year_of_birthday) + "-09-21"
  elif "winter" in the_season:
    the_birth_day = str(year_of_birthday) + "-12-21"
  else:
    the_birth_day = str(year_of_birthday) + "-01-01"  

  return the_birth_day

def process_one_line(one_line):
  a_species = ""
  a_sex = ""
  age_in_years = 99
  season = ""
  color = ""
  weight = ""
  origin_01 = ""
  origin_02 = ""

  print(one_line)
  groups_of_words = one_line.strip().split(", ")
  print(groups_of_words)
  single_words = groups_of_words[0].strip().split(" ")
  age_in_years = single_words[0]
  a_sex = single_words[3]
  a_species = single_words[4]
  single_words = groups_of_words[1].strip().split(" ")
  season = single_words[2]
  color = groups_of_words[2].strip()
  weight = groups_of_words[3].strip()
  origin_01 = groups_of_words[4].strip()
  origin_02 = groups_of_words[5].strip()


  from_zoo = origin_01 + ", " + origin_02

  birth_day = calc_birth_date(season, age_in_years)

  if "lion" in a_species:
    my_lion = Lion("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date) 
    my_lion.name = Lion.get_lion_name(my_lion)
    my_lion.animal_id = "Li" + str(Lion.numOfLions).zfill(2)
    list_of_lions.append(my_lion)

  if "tiger" in a_species:
    my_tiger = Tiger("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date) 
    my_tiger.name = Tiger.get_tiger_name(my_tiger)
    my_tiger.animal_id = "Ti" + str(Tiger.numOfTigers).zfill(2)
    list_of_tigers.append(my_tiger)

  if "hyena" in a_species:
    my_hyena = Hyena("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date) 
    my_hyena.name = Hyena.get_hyena_name(my_hyena)
    my_hyena.animal_id = "Hy" + str(Hyena.numOfHyenas).zfill(2)
    list_of_hyenas.append(my_hyena)  

  if "bear" in a_species:
    my_bear = Bear("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date) 
    my_bear.name = Bear.get_bear_name(my_bear)
    my_bear.animal_id = "Be" + str(Bear.numOfBears).zfill(2)
    list_of_bears.append(my_bear) 



file_path = "/Users/xel/Desktop/CIT-95/zooKeeperChallenge/arrivingAnimals.txt"
with open(file_path, "r") as file:
  for line in file:
    process_one_line(line)

print(f"\n\nNumber of animals created: {Animal.numOfAnimals}")
print(f"\n\nNumber of lions created: {Lion.numOfLions}")
print(f"\n\nNumber of tigers created: {Tiger.numOfTigers}")


print()
print("Zookeeper's Challenge Zoo Population")

print()
print("Lion Habitat:")
print()
for lion in list_of_lions:
  print(lion.animal_id + ", " + lion.name + "; birthdate: " + str(lion.birth_date) + "; " + lion.color + 
        "; " + lion.sex + "; " + lion.weight + "; " + lion.originating_zoo + "; arrived: " + str(lion.date_arrival))
  
print()
print("Tiger Habitat:")
print()
for tiger in list_of_tigers:
  print(tiger.animal_id + ", " + tiger.name + "; birthdate: " + str(tiger.birth_date) + "; " + tiger.color + 
        "; " + tiger.sex + "; " + tiger.weight + "; " + tiger.originating_zoo + "; arrived: " + str(tiger.date_arrival))
  
print()
print("Hyena Habitat:")
print()
for hyena in list_of_hyenas:
  print(hyena.animal_id + ", " + hyena.name + "; birthdate: " + str(hyena.birth_date) + "; " + hyena.color + 
        "; " + hyena.sex + "; " + hyena.weight + "; " + hyena.originating_zoo + "; arrived: " + str(hyena.date_arrival))
  
  print()
print("Bear Habitat:")
print()
for bear in list_of_bears:
  print(bear.animal_id + ", " + bear.name + "; birthdate: " + str(bear.birth_date) + "; " + bear.color + 
        "; " + bear.sex + "; " + bear.weight + "; " + bear.originating_zoo + "; arrived: " + str(bear.date_arrival))
