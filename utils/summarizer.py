def generate_summary(text):

    lines = text.split("\n")

    summary_lines = []

    for line in lines:
        if "I will" in line:
            summary_lines.append(line.strip())

    return " ".join(summary_lines[:3])