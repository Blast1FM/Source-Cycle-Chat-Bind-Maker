bind_name = input("Insert bind name (use (bind \"(the name you will input now)\" \"key\") it to bind your masterpiece to a key in tf2(or any source game for that matter) later):))\n")
bind_smol_name = input("This alias is not gonna see use in the end but needed to make the whole thing work(input anything you want, make sure it doesnt shadow anything you might have in your config already)\n")
counter = 0
with open("resultBind.txt", "w") as output:
    while True:
        output.write(f"alias {bind_smol_name}{counter} \"say {input()}; alias {bind_name} {bind_smol_name}{counter+1}\"\n")
        counter += 1
        print(f"you've typed {counter} lines already you stinky bastard, it's time to stop")
        checker = input("Keep going? literally anything/N: ")
        if checker == "N" or checker == "n":
            output.write(f"alias {bind_name} {bind_smol_name}0")
            break
