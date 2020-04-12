from os import remove

try:
    remove("lines.txt")
except FileNotFoundError:
    pass
    
bind_name = input("Insert bind name (use (bind \"(the name you will input now)\" \"key\") it to bind your masterpiece to a key in tf2(or any source game for that matter) later):))\n")
bind_smol_name = input("This alias is not gonna see use in the end but needed to make the whole thing work(input anything you want, make sure it doesnt shadow anything you might have in your config already)\n")
counter = 0


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


def block_input(bind_name, bind_smol_name, counter):
    end_phrase = input("End line:\n")
    global prev_input
    prev_input = ""
    with open("result_with_alias.txt", "w", encoding="utf-8") as output:
        while True:
            input_phrase = input()
            if input_phrase == end_phrase:
                break
            else:
                output.write(f"alias {bind_smol_name}{counter} \"say {input_phrase}; alias {bind_name} {bind_smol_name}{counter+1}\"\n")
                counter += 1
                prev_input = input_phrase
                with open("lines.txt", "a", encoding="utf-8") as phrase_output:
                    phrase_output.write(f"{input_phrase}\n")
        print(f"\nYou've typed {counter} lines, congratulations, you're a failure.\n")

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


def choose_input_mode():
    return input("How would you like to input your phrases? Type 1 for line by line input, 2 if you want to just paste a bunch of pre-formatted text in\nIf you try to paste a block of text with the line option selected, your script will not be generated properly\n")


input_mode = choose_input_mode()

if input_mode == "1":
    line_by_line_input(bind_name, bind_smol_name, counter)
elif input_mode == "2":
    block_input(bind_name, bind_smol_name, counter)
else:
    print("Invalid code, try again")
    choose_input_mode()