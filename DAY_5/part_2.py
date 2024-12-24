with open("input.txt") as file:
    rules_content, updates_content = file.read().split("\n\n")

rules = [rule.split("|") for rule in rules_content.split("\n")]

updates = [update.split(",") for update in updates_content.split("\n")]

middle_nums = []

for update in updates:
    applicable_rules = [
        rule for rule in rules if rule[0] in update and rule[1] in update
    ]
    violated_rule_locations = [
        (update.index(rule[0]), update.index(rule[1])) for rule in applicable_rules\
            if update.index(rule[0]) >= update.index(rule[1])
    ]
    if violated_rule_locations:
        for a, b in violated_rule_locations:
            temp = update[a]
            update[a] = update[b]
            update[b] = temp
        middle_nums.append(int(update[len(update)//2]))

print(sum(middle_nums))
