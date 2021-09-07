import random
import time

typemonlv1 = [
  "Wumper",
  "Tedder",
  "Leafalope",
  "Equester",
  "Phoomper",
  "Strick",
  "Jopa",
  "Chari",
  "Chucachi",
  "Noggar",
  "Tooth lily",
  "Pricklepig",
  "Krauka",
  "Xin",
  "light blob",
  "Triafish",
  "Lilanon",
  "Draklet",
  "Shonga",
  "Grappler"
]

typemonlv2 = [
  "Hiper",
  "Tumbler",
  "Pin-pon-pig",
  "Phoomy",
  "Niqua",
  "Ficenike",
  "Jompmon",
  "Chong",
  "Chukie",
  "Nograsaur",
  "Kraukzer",
  "Butterbloom",
  "Xin-hi",
  "Lilablossom",
  "Wobb-a-blob",
  "Trialight",
  "Drako",
  "Shang-ri",
  "Wrangler"
]

typemonlv3 = [
  "Snikemon",
  "Chol-zek",
  "Chu-zar",
  "Brauk",
  "Flower fly",
  "Xing-hoth",
  "Lil' paddy",
  "Blooper",
  "Shoc",
  "Maxigrab"
]

terrains = [
  "a pine_forest",
  "a jungle",
  "the grasslands",
  "the mountains",
  "a swamp",
  "a desert"
]

item_price = 0

shop = [
  "capsule holder",
  "luck coin",
  "knife",
  "gun",
  "ammo",
  "hp pack",
  "food"
]

class minilon():
  name = ""
  hp = 0
  damage = 0
  reward_for_kill = 0

class player():
  name = ""
  energy = 10
  hp = 100
  punch_damage = random.randrange(1, 10)
  stab_damage = 0
  shoot_damage = 0
  capsules = 0
  coins = random.randrange(10, 50)
  ammo = 0
  fight_actions = [
    "punch",
    "run",
    "catch"
  ]
  dead = False
  I_Caught_Em_All = False
  chance = 0
  searched = False
  found = False
  index = []
  inv = []

  def speak(speech):
    print(player.name + ': "' + speech + '"')
  
  def forage():
    if player.chance >= random.randrange(1, 100):
      print("You found some food!")
      player.inv.append("food")
    else:
      print("You didn't find anything edible.")
  
  def move(direction):
    if player.energy > 0:
      player.searched = False
      player.found = False
      player.energy -= 1
      rand_terrain = random.randrange(0, len(terrains))
      print(player.name + " moves " + direction)
      print("You are in " + terrains[rand_terrain])
      if terrains[rand_terrain] == terrains[0]:
        player.chance = random.randrange(30, 60)
      elif terrains[rand_terrain] == terrains[1]:
        player.chance = random.randrange(50, 80)
      elif terrains[rand_terrain] == terrains[2]:
        player.chance = random.randrange(10, 50)
      elif terrains[rand_terrain] == terrains[3]:
        player.chance = random.randrange(0, 40)
      elif terrains[rand_terrain] == terrains[4]:
        player.chance = random.randrange(20, 100)
      elif terrains[rand_terrain] == terrains[5]:
        player.chance = 0
      else:
        print("error")
    else:
      print("You have no energy!")
    
    print("You have " + str(player.chance) + " chance of finding a minilon.")

  def fight():
    if player.found == True:
      print(player.name + " decides to fight a " + minilon.name + " with " + str(minilon.hp) + " hp!")
      while True:
        print("What does " + player.name + " do?")
        y = 1
        for x in player.fight_actions:
          print(str(y) + ". " + x)
          y += 1

        choose_action = input("")
        if str(choose_action) in player.fight_actions:
          if choose_action == "punch":
            print(player.name + " punches the " + minilon.name)
            if random.randrange(0, 10) >= 2:
              print("they hit!")
              minilon.hp -= player.punch_damage
              print(minilon.name + " has " + str(minilon.hp) + " hp left!")
            else:
              print("they miss!")
          elif "knife" in player.inv and choose_action == "stab":
            print(player.name + " stabs the " + minilon.name)
            if random.randrange(0, 10) >= 5:
              print("they hit!")
              minilon.hp -= player.stab_damage
              print(minilon.name + " has " + str(minilon.hp) + " hp left!")
            else:
              print("they miss!")
          elif "gun" in player.inv and choose_action == "shoot":
            print(player.name + " shoots the " + minilon.name)
            if random.randrange(0, 10) >= 7:
              if player.ammo > 0:
                print("they hit!")
                player.ammo -= 1
                minilon.hp -= player.shoot_damage
                print(minilon.name + " has " + str(minilon.hp) + " hp left!")
              else:
                print("You don't have any ammo!")
            else:
              player.ammo -= 1
              print("they miss!")
          elif choose_action == "run":
            print("You run away.")
            break
          elif player.capsules > 0 and choose_action == "catch":
            print("You throw a capsule at the creature in hopes of catching it!")
            player.capsules -= 1
            if minilon.hp <= 10:
              print("It worked! The minilon has been added to your index!")
              player.index.append(minilon.name)
              if minilon.name in typemonlv1:
                typemonlv1.remove(minilon.name)
                break
              elif minilon.name in typemonlv2:
                typemonlv2.remove(minilon.name)
                break
              elif minilon.name in typemonlv3:
                typemonlv3.remove(minilon.name)
                break
            else:
              print("The " + minilon.name + " dodged the capsule. It still has too much hp.")
          else:
            print("You do nothing.")
          # check if the minilon is dead yet!
          if minilon.hp <= 0:
            print("You won the battle!")
            print("You recieved " + str(minilon.reward_for_kill) + " coins!")
            player.coins += minilon.reward_for_kill
            break

          print("The minilon attacks!")
          time.sleep(1)
          if minilon.name in typemonlv1:
            if random.randrange(0, 10) <= 4:
              print("He hits!")
              player.hp -= minilon.damage
              print(player.name + " has " + str(player.hp) + " hp left!")
            else:
              print("He misses!")
          elif minilon.name in typemonlv2:
            if random.randrange(0, 10) <= 5:
              print("He hits!")
              player.hp -= minilon.damage
              print(player.name + " has " + str(player.hp) + " hp left!")
            else:
              print("He misses!")
          elif minilon.name in typemonlv3:
            if random.randrange(0, 10) <= 6:
              print("He hits!")
              player.hp -= minilon.damage
              print(player.name + " has " + str(player.hp) + " hp left!")
            else:
              print("He misses!")
            
          if player.hp <= 0:
            print("The " + minilon.name + " killed you.")
            player.dead = True
            break
            
    else:
      print("You haven't found any minilons!")
  
  def search():
    if player.searched == False:
      print("You search and")
      if "luck coin" in player.inv:
        player.chance += random.randrange(1, 20)
      if len(typemonlv1) != 0:
        if player.chance >= random.randrange(20, 100):
          print(" see a " + typemonlv1[rand_lv1] + "!")
          player.searched = True
          player.found = True
          minilon.name = typemonlv1[rand_lv1]
          minilon.hp = random.randrange(20, 50)
          minilon.damage = random.randrange(1, 10)
          minilon.reward_for_kill = random.randrange(20, 50)
        else:
          print(" see nothing.")
          player.searched = True
      elif len(typemonlv2) != 0:
        if player.chance >= random.randrange(50, 100):
          print(" see a " + typemonlv2[rand_lv2] + "!")
          player.searched = True
          player.found = True
          minilon.name = typemonlv2[rand_lv2]
          minilon.hp = random.randrange(50, 80)
          minilon.damage = random.randrange(20, 30)
          minilon.reward_for_kill = random.randrange(50, 80)
        else:
          print(" see nothing.")
          player.searched = True
      else:
        if player.chance >= random.randrange(80, 100):
          print(" see a " + typemonlv3[rand_lv3] + "!")
          player.searched = True
          player.found = True
          minilon.name = typemonlv3[rand_lv3]
          minilon.hp = random.randrange(80, 100)
          minilon.damage = random.randrange(30, 50)
          minilon.reward_for_kill = random.randrange(100, 200)
        else:
          print(" see nothing.")
          player.searched = True
    else:
      print("You searched already!")

  def buy(item):
    if item in shop:
      print(player.name + " buys a " + item)
      if item_price <= player.coins:
        if item not in player.inv:
          player.coins -= item_price
          player.inv.append(item)
        else:
          print("You already own that object!")
      else:
        print("You don't have enough money to buy that!")
    else:
      print("That's not in the shop!")
  
  def use(item):
    if item in player.inv:
      if item == "capsule holder":
        print("You open the capsule holder and gain 10 capsules!")
        player.capsules += 10
        player.inv.remove("capsule holder")
      elif item == "knife":
        print("You equip your knife. You are now more dangerous.")
        player.stab_damage = random.randrange(11, 20)
        player.fight_actions.insert(1, "stab")
      elif item == "gun":
        print("You equip your gun. You are now way more dangerous 0__0")
        player.shoot_damage = random.randrange(15, 28)
        if len(player.fight_actions) >= 5:
          player.fight_actions.insert(2, "shoot")
        else:
          player.fight_actions.insert(1, "shoot")
      elif item == "hp pack":
        print("You use the hp pack! You regenerate your strength!")
        player.hp = 100
        player.inv.remove("hp pack")
      elif item == "ammo":
        player.ammo += random.randrange(10, 15)
        print("you load your gun! You now have " + str(player.ammo) + " ammo!")
        player.inv.remove("ammo")
      elif item == "food":
        player.energy += random.randrange(10, 15)
        print("You ate and regained strength! You now have " + str(player.energy) + " energy!")
        player.inv.remove("food")
      else:
        print("You can't use that!")
    else:
      print("You don't have any such thing!")

#leadup thing
print("Prof R: Hello. \n I heard that you wanted to save the world. If you're coming from the lead-up, Wellcome! \n If you have no idea what I am talking about, you can go here " + '\n https://replit.com/talk/share/The-big-lead-up/145033' + "\n On to the story...")
time.sleep(5)
print("What was your name again?")
player.name = input("")

print("Oh. It was " + player.name + ", was it? Anyway, I hope you have luck catching the minilons!")
time.sleep(3)

print("Oh, and before I forget, here are a couple capsules to help you along!")
player.capsules += 5
print("You now have " + str(player.capsules) + " capsules!")
time.sleep(3)
print("Remember, you have to catch all the minilons and bring them to me.")
types = [
  "move",
  "fight",
  "shop",
  "inv",
  "search",
  "stats",
  "index",
  "use",
  "forage"
]

# Start The Game!
while player.dead == False:

  rand_lv1 = random.randrange(0, len(typemonlv1))
  rand_lv2 = random.randrange(0, len(typemonlv2))
  rand_lv3 = random.randrange(0, len(typemonlv3))
  time.sleep(2)
  print("")
  print("What do you want to do?")
  for x in types:
    print("~" + x)
  what_to_do = input("~")
  #command to move
  time.sleep(1)
  if what_to_do == "move":
    print("Which direction do you want to move?\n~north\n~south\n~east\n~west")
    direction = input("~")
    # move north
    if direction == "north":
      player.move("north")
    # move south
    elif direction == "south":
      player.move("south")
    # move east
    elif direction == "east":
      player.move("east")
    # move west
    elif direction == "west":
      player.move("west")
    else:
      print("That's not a direction!")
  # fight a minilon
  elif what_to_do == "fight":
    player.fight()
  # shop for supplies
  elif what_to_do == "shop":
    print("Shopkeeper: What can I do for you today?")
    time.sleep(2)
    player.speak("I'd like to buy something.")
    time.sleep(2)
    print("Shopkeeper: This is what we have for sale... tell me what you want to buy.")
    for x in shop:
      print("~" + x)
    item = input("")
    if item == shop[0]:
      item_price = 10
      player.buy(item)
    elif item == shop[1]:
      item_price = 15
      player.buy(item)
    elif item == shop[2]:
      item_price = 30
      player.buy(item)
    elif item == shop[3]:
      item_price = 50
      player.buy(item)
    elif item == shop[4]:
      item_price = 20
      player.buy(item)
    elif item == shop[5]:
      item_price = 5
      player.buy(item)
    elif item == shop[6]:
      item_price = 8
      player.buy(item)
    else:
      print("Error")
  # display inventory
  elif what_to_do == "inv":
    if len(player.inv) != 0:
      y = 1
      for x in player.inv:
        print(str(y) + ". " + x)
        y += 1
    else:
      print("You don't have any items!")
  # search for minilons
  elif what_to_do == "search":
    player.search()
  # display stats
  elif what_to_do == "stats":
    print(player.name + " has " + str(player.hp) + " hp.")
    print(player.name + " has " + str(player.energy) + " energy.")
    print(player.name + " has " + str(player.coins) + " coins to spend.")
    print(player.name + " has " + str(player.capsules) + " capsules left.")
    print(player.name + " has " + str(player.punch_damage) + " punch-power.")
    if player.stab_damage != 0:
      print(player.name + " has " + str(player.stab_damage) + " stabbing power!")
    if player.shoot_damage != 0:
      print(player.name + " has " + player.shoot_damage + " shooting power!")
  # display caught minilons
  elif what_to_do == "index":
    if len(player.index) != 0:
      y = 1
      for x in player.index:
        print(str(y) + ". " + x)
        time.sleep(2)
        y += 1
    else:
      print("You don't have any minilons!")
  # use an item in your inv
  elif what_to_do == "use":
    print("What do you want to use?")
    what_to_use = input("")
    player.use(what_to_use)
  # forage for food
  elif what_to_do == "forage":
    player.forage()

  else:
    print("That's not a valid option!")
  
  if len(typemonlv3) == 0 and len(typemonlv2) == 0 and len(typemonlv1) == 0:
    player.I_caught_Em_All = True
    break

if player.dead == True:
  print("You died!")
elif player.I_Caught_Em_All == True:
  print("FINALLY!!! After all this time, you have finally caught every minilon!")
  time.sleep(4)
  print("You hurry back to Prof R.")
  time.sleep(2)
  player.speak("I caught them all professor!!!")
  time.sleep(2)
  print("Prof R: WOW! I never thought you could do it so quickly!")
  time.sleep(3)
  print("He looks at all your capsules.")
  time.sleep(2)
  player.speak("Here you go, professor!")
  time.sleep(2)
  print("You hand over the capsules and the next day, prof R is able to attract all the minilons back to his lab.")
  time.sleep(5)
  print("You saved the world!")
  print("or... so you thought...")
  time.sleep(3)
  print("Prof R: Wake up ," + player.name + "!")
  time.sleep(2)
  player.speak("Wha? Prof? Did the minilons escape again?!")
  time.sleep(3)
  print("Prof R: No, No, Not that, but in a way, it might be better than what did happen!!!")
  time.sleep(2)
  player.speak("What did happen?")
  time.sleep(2)
  print("Prof R: I ")
  time.sleep(5)
  print("...")
  time.sleep(2)
  print("To be continued...")
  time.sleep(3)
  print("Me: That's the end! I hope you enjoyed this game! Please stay tuned for next time! BYE!")