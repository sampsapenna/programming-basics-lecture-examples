"""Example on formatting a table."""

table_header = "{:>30.20s} {:>50.40s} {:>30.20s}".format(
    "Etunimi",
    "Sukunimi",
    "Asuinpaikka",
)

first_name_1 = "Arron"
last_name_1 = "Waller"
place_of_residence_1 = "Manchester"

first_name_2 = "Logan"
last_name_2 = "O'Donnell"
place_of_residence_2 = "Leeds"

first_name_3 = "Honor"
last_name_3 = "Marshall"
place_of_residence_3 = "Scarborough"

first_name_4 = "Jenson"
last_name_4 = "Lane"
place_of_residence_4 = "Stoke-on-Trent"

first_name_5 = "Elodie"
last_name_5 = "Ingram"
place_of_residence_5 = "Newcastle"

table_row = "{:>30.20s} {:>50.40s} {:>30.20s}"

print(table_header)
print(table_row.format(
    first_name_1,
    last_name_1,
    place_of_residence_1,
))
print(table_row.format(
    first_name_2,
    last_name_2,
    place_of_residence_2,
))
print(table_row.format(
    first_name_3,
    last_name_3,
    place_of_residence_3,
))
print(table_row.format(
    first_name_4,
    last_name_4,
    place_of_residence_4,
))
print(table_row.format(
    first_name_5,
    last_name_5,
    place_of_residence_5,
))

print("\n\n\n")

filesystem_table_row = "{:10.10s} {:6d} {:10.10s} {:10.10s} {:15.15s} {:s}"

access_rights_1 = "-rw-rw-r--"
links_1 = 1
user_1 = "sampsa"
group_1 = "sampsa"
size_1 = "51"
last_modified_1 = "Sep 15 12:36"
filename_1 = "constants.py"

access_rights_2 = "-rw-rw-r--"
links_2 = 1
user_2 = "sampsa"
group_2 = "sampsa"
size_2 = "103"
last_modified_2 = "Sep 15 13:10"
filename_2 = "examples.py"

access_rights_3 = "-rw-rw-r--"
links_3 = 1
user_3 = "sampsa"
group_3 = "sampsa"
size_3 = "1.1K"
last_modified_3 = "Sep 15 14:00"
filename_3 = "table_formatting.py"

access_rights_4 = "-rw-rw-r--"
links_4 = 1
user_4 = "sampsa"
group_4 = "sampsa"
size_4 = "221"
last_modified_4 = "Sep 15 12:59"
filename_4 = "variables.py"

print("{:10.10s} {:6.5s} {:10.10s} {:10.10s} {:15.15s} {}".format("Access", "Links", "User", "Group", "Modified", "Filename"))
print(filesystem_table_row.format(
    access_rights_1,
    links_1,
    user_1,
    group_1,
    last_modified_1,
    filename_1,
))
print(filesystem_table_row.format(
    access_rights_2,
    links_2,
    user_2,
    group_2,
    last_modified_2,
    filename_2,
))
print(filesystem_table_row.format(
    access_rights_3,
    links_3,
    user_3,
    group_3,
    last_modified_3,
    filename_3,
))
print(filesystem_table_row.format(
    access_rights_4,
    links_4,
    user_4,
    group_4,
    last_modified_4,
    filename_4,
))

print("\n\n\n")
print("Access     Links  User       Group      Modified        Filename")
print(f"{access_rights_1:10.10s} {links_1:6d} {user_1:10.10s} {group_1:10.10s} {last_modified_1:15.15s} {filename_1}")
print(f"{access_rights_2:10.10s} {links_2:6d} {user_2:10.10s} {group_2:10.10s} {last_modified_2:15.15s} {filename_2}")
print(f"{access_rights_3:10.10s} {links_3:6d} {user_3:10.10s} {group_3:10.10s} {last_modified_3:15.15s} {filename_3}")
print(f"{access_rights_4:10.10s} {links_4:6d} {user_4:10.10s} {group_4:10.10s} {last_modified_4:15.15s} {filename_4}")
