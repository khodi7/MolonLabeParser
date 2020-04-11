import os

save_path = "C:\\Users\\Utilisateur\\Documents\\Paradox Interactive\\Imperator\\save games"
save_name = "DaF_DOA-3.0.rome"
output_file = "DaF_DOA-3.1.rome"
os.chdir(save_path)

with open(save_name, "r") as file:
    content = file.readlines()
for i in range(len(content)-1, -1, -1):
    line = content[i]
    if line.count("=") == 1 and line.split("=")[0].strip() == "claim":
        del content[i]
with open(output_file, "w") as file:
    file.writelines(content)