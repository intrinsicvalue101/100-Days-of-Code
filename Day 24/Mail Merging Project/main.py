name_list = []
PLACEHOLDER = "[name]"

# create list of names reading the file line by line
# ./ --> currentfolder
with open("./Names/invited_names.txt") as names_file:
    for line in names_file:
        name_list.append(line.strip()) # strip removes special characters/whitespaces
# print(name_list)

with open("./Letters/starting_letter.txt", mode="r") as email_template:
    content = email_template.read()
    for name in name_list:
        new_content = content.replace(PLACEHOLDER, f"{name}")
        with open(f"./ReadyToSend/letter_for_{name}.txt", mode="w") as new_file:
            new_file.write(new_content)
