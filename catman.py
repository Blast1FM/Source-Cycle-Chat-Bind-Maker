from os import remove

try:
    remove("lines.txt")
except FileNotFoundError:
    pass
    
bind_name = input("Insert bind name (use (bind \"(the name you will input now)\" \"key\") it to bind your masterpiece to a key in tf2(or any source game for that matter) later):))\n")
bind_smol_name = input("This alias is not gonna see use in the end but needed to make the whole thing work(input anything you want, make sure it doesnt shadow anything you might have in your config already)\n")
counter = 0

with open("result_with_alias.txt", "w", encoding="utf-8") as output:
    while True:
        input_phrase = input()
        output.write(f"alias {bind_smol_name}{counter} \"say {input_phrase}; alias {bind_name} {bind_smol_name}{counter+1}\"\n")
        with open("lines.txt", "a", encoding="utf-8") as phrase_output:
            phrase_output.write(f"{input_phrase}\n")
        counter += 1
        print(f"You've typed {counter} lines, it's time to stop.\n")
        checker = input("Keep going? Anything/N: ")
        if checker == "N" or checker == "n":
            break

with open("result_final.txt", "w", encoding="utf-8") as output:
    with open("result_with_alias.txt", encoding="utf-8") as input:
        for line in input:
            if line != f"alias {bind_smol_name}{counter-1} \"say {input_phrase}; alias {bind_name} {bind_smol_name}{counter}\"\n":
                output.write(line)
            else:
                output.write(f"alias {bind_smol_name}{counter-1} \"say {input_phrase}; alias {bind_name} {bind_smol_name}0\"\n")
                output.write(f"alias {bind_name} {bind_smol_name}0\n")
                output.write(f"bind \"Your_key\" {bind_name}\n")

remove("result_with_alias.txt")
