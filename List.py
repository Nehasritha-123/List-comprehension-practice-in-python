fruits = ["Nuts", "mango", "Nectarine", "orange" ,"Pears", "Nance" ]
# Filtering only fruits that start with 'N'
N_fruits = [x for x in fruits if x.startswith("N")]
print("List of 'N' fruits from original:", N_fruits)