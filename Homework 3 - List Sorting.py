print("********** List Sorting **********\n\n\n")
try:
 with open("football player.txt","r+") as player:
  while True:
    data=player.readline()
    if "Galatasaray" in data:
        with open("Galatasaray team.txt","a")as gs:
            gs.write(data)
    elif "Fenerbahce" in data:
        with open("Fenerbahce team.txt","a")as fb:
            fb.write(data)
    elif "Besiktas" in data:
        with open("Besiktas team.txt","a") as bjk:
            bjk.write(data)
    else:
        break
except FileNotFoundError as error:
 print("Source file not found. Please check source file")
 print(error)
 
