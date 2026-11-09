# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Micah Kadiri
#               Benjamin Hatch
#               Ajay Palanisamy
#               Hudson Dobb
#               Mayu Kotwal
# Section:      508
# Assignment:   Lab Topic 11 (Team)
# Date:         11 November 2026
#
# My Code
xp = input("Enter the name of the file: ")
fp = open(xp)
passports = fp.read().strip("\n").split("\n\n")
fp.close()

req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "cid"]
count = 0
out = open("valid_passports2.txt", "w")

for p in passports:
    fields = {}
    for field in p.split():
        key, value = field.split(":", 1)
        fields[key] = value

    valid = True
    for r in req:
        if r not in fields:
            valid = False

    if not valid:
        continue

    # Check that each year has four digits before converting it.
    for r in ["byr", "iyr", "eyr"]:
        value = fields[r]
        if len(value) != 4:
            valid = False
        for c in value:
            if c not in "0123456789":
                valid = False

    if not valid:
        continue

    if not 1922 <= int(fields["byr"]) <= 2010:
        valid = False
    if not 2016 <= int(fields["iyr"]) <= 2026:
        valid = False
    if not 2026 <= int(fields["eyr"]) <= 2036:
        valid = False

    # Check the height's number and unit.
    height = fields["hgt"]
    number = height[:-2]
    unit = height[-2:]
    if number == "":
        valid = False
    for c in number:
        if c not in "0123456789":
            valid = False

    if valid:
        if unit == "cm":
            if not 150 <= int(number) <= 193:
                valid = False
        elif unit == "in":
            if not 59 <= int(number) <= 76:
                valid = False
        else:
            valid = False

    # Check hair color and eye color.
    hair = fields["hcl"]
    if len(hair) != 7 or hair[0] != "#":
        valid = False
    else:
        for c in hair[1:]:
            if c not in "0123456789abcdef":
                valid = False

    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if fields["ecl"] not in eye_colors:
        valid = False

    # Country ID must be three digits without a leading zero.
    country = fields["cid"]
    if len(country) != 3 or country[0] == "0":
        valid = False
    for c in country:
        if c not in "0123456789":
            valid = False

    if valid:
        if count > 0:
            out.write("\n")
        out.write(p.strip("\n") + "\n")
        count += 1

out.close()
print(f"There are {count} valid passports")
