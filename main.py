Sword = False
fighting_ability = False
key = False
bannedfromvillage = False

pathway1 = input("Welcome to the Treasure Island\nYou awake to find yourself in a clearing, you aren't sure where you are. There are two paths ahead. A long winding path that is bright or an overgrown and dark incline.\nEnter 'Up' or 'Down' to choose a path.\n")
if pathway1 =="Down":
 print("\nYou head down the long winding path, the sounds of seagulls begin to fill the air and salt stings your nose. You find yourself stumbling into a beach. The tide is low, and there looks to be a village above the cliffside.\n")
 Seashell_Choice = input("\nThere is a small seashell not too far from where you stand, would you like to pick it up? \nY or N\n")
 if Seashell_Choice == "Y":
  Seashell = 1
 if Seashell_Choice == "N":
   print("\nYou decide against it, placing the shell back on the sand.\n")
   Seashell = 0
 pathway2 = input("\nWould you like to head to the village, or continue along the beach?\nEnter 'Beach' or 'Village' to continue\n")
 if pathway2 == "Beach":
  print("\nYou continue down the beach, the warm sun comforting on your back. While you're enjoying the view, you suddenly come across a large hulking orc. He looks far above your level, and you don't have a sword. Before you are able to sneak away, he notices you.\n")
  Orc_Battle = input("\nWould you like to fight him or talk to him?\nEnter 'Fight' or 'Talk'\n")
  if Orc_Battle == "Fight":
    print("\nYou let out a war cry as you charge forward, smacking your palms against his ankle. The orc watches, before laughing. He approves of your spirit and offers entry to the rest of the beach, or the shortcut to the village. Behind him, you notice something glinting in the sun. The Orc sits back down and continues to sunbathe.\n")
    pathway3 = input("\nWould you like to attempt to steal the glinting object or would you like to check out the village?\nEnter 'Steal' or 'Village'\n")
    if pathway3 == "Steal":
     print("\nYou have stolen a silver key, it looks important. You sneak to the village before he notices your attempt\n")
    pathway2 = "Village"
    key = True
  else:
    print("\nYou tell the Orc you intend no harm, and he begins to walk towards you. You tell him how you woke up in the clearing, and that you have no belongings\n")
    if Seashell == 1:
      print("\nThe Orc notices the seashell, and decides you are untruthful. He squashes you with his bat without a second thought.\n The End - Ending (Orc Soup)")
    if Seashell == 0:
     print("\nThe Orc considers your words, before smacking you with his bat. There's no room on the island for castaways after all.\n The End - Ending (Orc Soup 2)")
  
 if pathway2 == "Village":
   print("\nThe village is bright and cheerful, there are children running around and jolly drunks at the pub. You notice a shop that looks like it sells weapons. You are sure you can convince the owner to spare a sword\n")
   print("\nYou enter the shop, an array of weapons line the walls and you nod appreciatively. Sat at the far wall, the swordsmith greets you. You begin to tell him your story. He looks increasingly more annoyed. Finally, he demands to knowif you're going to be paying or not.\n")
   if Seashell == 1:
    print("\nYou remember the seashell in your pocket and offer it to him. He looks it over before nodding and directing you to a small sword. It doesn't look the most sturdy, but it's a sword. You thank him and leave the shop.\n")
    pathway1 = "Up"
    Sword = True 
   else:
     print("\nYou realise your mistake, and begin to plead with the man. You promise to find treasure that would be worth his while. Growing more angry, the swordsmith has the guards arrest you.\n")
     prison_choice = input("\nYou awake to find yourself in a prison, would you like to try to escape? Or would you like to spend your sentence. \nEnter 'Escape' or'Sentence\n")
     if prison_choice == "Escape":
      print("\nYou manage to slip past the jailors, and make a break for an inclined path. While hiding from the pursuing guards, you find a rusty sword.\n")
      bannedfromvillage = True
      Sword = True
      pathway1 = "Up"
     else:
      print("\nYou spend your remaining prison sentence settling in, you befriend the nearby inmate who teach you how to fight. You make some great friends. Before you know it, time is up. You get released into an inclined path.\n")
      fighting_ability = True
      pathway1 = "Up"

if pathway1 == "Up":
  print("\nYou find youself at a steeper and steeper incline. Looking back down the path, you notice you've begun climbing a mountain. Not so far away, you hear a loud conversation.\n")
  print("\nThe travellers are loudly talking about a treasure being guarded by a dragon.\n")
  dragon_choice = input("\nWould you like to fight the dragon or attempt to steal the treasure while he sleeps? \nEnter 'Fight' or 'Steal' \n")
  if dragon_choice == "Fight":
    if Sword == True or fighting_ability == True:
      print("\nYou decide to fight the dragon. \nYou set off straight away to the dragon, confidence in your step. You approach the beasts resting place and let out a loud yell. The dragon stirs and a long battle ensues. \nThe dragon proves to be no match for your strength. You manage to defeat the dragon. Behind him, you notice a silver chest.\n")
      if key == True:
        print("\nYou pull out the silver key you stole from the orc, grinning victoriously. Upon opening the chest, you find a wealth of gold. You're set for life! \n The End - Ending 'True Capitalist'")
      else:
        if bannedfromvillage == True:
          print("\nYou begin grinning, stumbling over to the chest. However, a lock is present. You can't open it. You frown, then remember the swordsmith. Perhaps he can open the chest! \nAfter making your way to the village with the heavy chest, you enter the shop once more. The man sees you, remembers you, and worst of all he calls the guards before you can explain! Your chest gets confiscated and you find yourself once more in jail. Unfortunately, this time escape seems impossible. \nThe End. Ending - Criminal scum!")
        else:
          print("\nYou begin grinning, stumbling over to the chest. However, a lock is present. You can't open it. You frown, then remember the swordsmith. Perhaps he can open the chest! \nAfter making your way to the village with the heavy chest, you enter the shop once more. The shopkeep recognises you and nods towards you. You show him the chest and promise him 50% if he can open it for you. He opens the chest and you share the profits. You're well off enough to enjoy the rest of your time on the island. \n The End! Ending - Shopkeepers Best Friend.")
    else:
      print("\nYou decide to fight the dragon. \nYou set off straight away to the dragon, confidence in your step. You approach the beasts resting place and let out a loud yell. The dragon stirs and a long battle ensues. \nYet, without a sword or any fighting ability at all. You quickly find yourself beaten. The dragon has no mercy and eats you in one. \nThe End. Ending - The opportunist.")
  else:
    print("\nYou find the resting place of the beast and wait until dark. Using the dark of the night, you sneak over to a glistening silver chest. However, before you can take it, the dragon eats you in one. \n The End. Ending - The Nocturnal Dragon")