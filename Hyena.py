from Animal import Animal

class Hyena(Animal):
  numOfHyenas = 0

  hyena_sound = "eek_eek"

  list_of_hyena_names = []  

  file_path = "/Users/xel/Desktop/CIT-95/zooKeeperChallenge/animalNames.txt"
  with open(file_path, 'r') as file:
    lines = file.readlines()

    line_num = 1
    for line in lines:
      if line_num == 3:
        list_of_hyena_names.extend(line.strip().split(', '))
        break
      else:
        line_num += 1
  
  def __init__(self, name ="a_name", animal_id = "an_id", birth_date = "2099-01-01", color = "a_color", sex = "a_sex", 
               weight = "a_weight", originating_zoo = "a_zoo", date_arrival = "2099-01-01"):
    Hyena.numOfHyenas +=1
    super().__init__("hyena", name, animal_id, birth_date, color, sex, weight, originating_zoo, date_arrival)

  def make_sound(self):
    return self.hyena_sound
  
  def get_hyena_name(self):
    return self.list_of_hyena_names.pop(0)