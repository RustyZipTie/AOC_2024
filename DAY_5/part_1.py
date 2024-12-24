with open("input.txt") as file:
    rules_content, updates_content = file.read().split("\n\n")

rules = [rule.split("|") for rule in rules_content.split("\n")]

updates = [update.split(",") for update in updates_content.split("\n")]

middle_nums = []

for update in updates:
    in_order = True
    applicable_rules = [
        rule for rule in rules if rule[0] in update and rule[1] in update
    ]
    for rule in applicable_rules:
        if update.index(rule[0]) >= update.index(rule[1]):
            in_order = False
            break
    if in_order:
        middle_nums.append(int(update[len(update)//2]))

print(sum(middle_nums))
