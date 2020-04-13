from os import remove
from time import sleep

try:
    remove("lines.txt")
except FileNotFoundError:
    pass
    
bind_name = input("Insert bind name (use (bind \"(the name you will input now)\" \"key\") it to bind your masterpiece to a key in tf2(or any source game for that matter) later):))\n")
bind_smol_name = input("This alias is not gonna see use in the end but needed to make the whole thing work(input anything you want, make sure it doesnt shadow anything you might have in your config already)\n")
counter = 0        

def block_input(bind_name, bind_smol_name, counter):
    end_phrase = input("End line:\n")
    global prev_input
    prev_input = ""
    with open("result_with_alias.txt", "w", encoding="utf-8") as output:
        while True:
            input_phrase = input()
            if input_phrase == end_phrase:
                break
            elif input_phrase.strip()!="":
                output.write(f"alias {bind_smol_name}{counter} \"say {input_phrase}; alias {bind_name} {bind_smol_name}{counter+1}\"\n")
                counter += 1
                prev_input = input_phrase
                with open("lines.txt", "a", encoding="utf-8") as phrase_output:
                    phrase_output.write(f"{input_phrase}\n")
            else:
                pass
        print(f"\nYou've typed {counter} line(s). Congratulations, people will hate you.\nMade by BlastFM and I don't regret anything\n")

    with open("result_final.txt", "w", encoding="utf-8") as output:
        with open("result_with_alias.txt", encoding="utf-8") as inputs:
            for line in inputs:
                if line != f"alias {bind_smol_name}{counter-1} \"say {prev_input}; alias {bind_name} {bind_smol_name}{counter}\"\n":
                    output.write(line)
                else:
                    output.write(f"alias {bind_smol_name}{counter-1} \"say {prev_input}; alias {bind_name} {bind_smol_name}0\"\n")
                    output.write(f"alias {bind_name} {bind_smol_name}0\n")
                    output.write(f"bind \"Your_key\" {bind_name}\n")
        remove("result_with_alias.txt")

block_input(bind_name, bind_smol_name, counter)


""" Useless input method hoo hoo but i spent too much time on it so i'm leaving it in as a comment and a sign of my stupidity
def line_by_line_input(bind_name, bind_smol_name,counter):
    with open("result_with_alias.txt", "w", encoding="utf-8") as output:
        end_phrase = input("End line:\n")
        global prev_input
        prev_input = ""
        while True:
            input_phrase = input()
            if input_phrase != end_phrase:
                output.write(f"alias {bind_smol_name}{counter} \"say {input_phrase}; alias {bind_name} {bind_smol_name}{counter+1}\"\n")
                with open("lines.txt", "a", encoding="utf-8") as phrase_output:
                    phrase_output.write(f"{input_phrase}\n")
                prev_input = input_phrase
                counter += 1
                print(f"You've typed {counter} lines, it's time to stop.")
            else:
                break

    with open("result_final.txt", "w", encoding="utf-8") as output:
        with open("result_with_alias.txt", encoding="utf-8") as inputs:
            for line in inputs:
                if line != f"alias {bind_smol_name}{counter-1} \"say {prev_input}; alias {bind_name} {bind_smol_name}{counter}\"\n":
                    output.write(line)
                else:
                    output.write(f"alias {bind_smol_name}{counter-1} \"say {prev_input}; alias {bind_name} {bind_smol_name}0\"\n")
                    output.write(f"alias {bind_name} {bind_smol_name}0\n")
                    output.write(f"bind \"Your_key\" {bind_name}\n")
        remove("result_with_alias.txt")
"""

print("Success. Don't forget to bind the main alias to a key. Exiting in 6.94201337 seconds")

sleep(6.94201337)
