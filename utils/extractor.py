def extract_action_items(text):
    action_items = []

    lines = text.split("\n")

    for line in lines:
        if "I will" in line:
            action_items.append(line.strip())

    return action_items