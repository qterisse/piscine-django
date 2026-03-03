import sys

def parse_file(file_content: str):
    elements = []
    required_keys = ["name", "number", "position", "small", "molar", "electron"]

    for line in file_content.split("\n"):
        if (len(line) == 0 or not "=" in line):
            continue

        element_name, properties_part = line.split("=", 1)

        element_name = element_name.strip()
        properties_part = properties_part.strip()

        element = {'name': element_name}
        for item in properties_part.split(","):
            key, value = item.split(":", 1)
            element[key.strip()] = value.strip()
        
        if any([not k in element for k in required_keys]):
            continue

        elements.append(element)
    
    return elements

def build_html_table(elements: dict):
    table = "<table>"
    row = "\t\t<tr>"

    y = 0
    nb_electrons = 1
    for element in elements:
        if (len(element["electron"].split(" ")) > nb_electrons):
            table += "\n" + row + "\n\t\t</tr>"
            row = "\t\t<tr>"
            nb_electrons += 1
            y = 0
        
        position = int(element["position"])
        while (position != y and y < 17):
            row += '\n\t\t\t<td class="empty"></td>'
            y += 1

        td = f"""\t\t\t<td>
\t\t\t\t<ul class="top-data"><li>{element["number"]}</li><li>{round(float(element["molar"]), 1)}</li></ul>
\t\t\t\t<h4>{element["small"]}</h4>
\t\t\t\t<p>{element["name"]}</p>
\t\t\t</td>"""

        row += "\n" + td
        y += 1
    
    table += "\n</table>"
    return table

def create_html_file(table: str):
    html_file_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
\t<meta charset="UTF-8">
\t<meta name="viewport" content="width=device-width, initial-scale=1.0">
\t<title>Tableau périodique</title>
\t<link href="./periodic.css" rel="stylesheet">
</head>
<body>
    {table}
</body>
</html>"""

    with open("periodique.html", "w") as f:
        f.write(html_file_content)


def main(periodic_file: str):
    try:
        f = open(periodic_file, "r")
    except:
        print(f"\033[91mERROR\033[0m: Input file {periodic_file} could not be found")
    
    elements = parse_file(f.read())
    table = build_html_table(elements)
    create_html_file(table)

    f.close()

if __name__ == "__main__":
    periodic_file = "periodic_table.txt"
    if len(sys.argv) == 2:
        periodic_file = argv[1]
    
    main(periodic_file)