with open("c:/Users/spide/Desktop/Technikum/INformatyka/klasa 3/06/slowa_06.txt", "r", encoding="utf-8") as infile, \
     open("c:/Users/spide/Desktop/Technikum/INformatyka/klasa 3/06/slowa_numerowane.txt", "w", encoding="utf-8") as outfile:
    
    for word in enumerate(infile):
        outfile.write(f"{word}\n")
