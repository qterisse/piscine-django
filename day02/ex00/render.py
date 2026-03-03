from settings import *
import sys

def replaceAll(text, replaceBy):
    for key in replaceBy:
        regex = "{" + key + "}"
        if (regex in text):
            text = text.replace(regex, replaceBy[key])
    
    return text

def main(template_file):
    try:
        with open(template_file) as f:
            text = f.read()
    except:
        print("Could not open the file" + template_file)
        exit()

    exclude = ["sys", "replaceAll", "main"]
    settings = {k:v for k,v in dict(globals()).items() if not k.startswith("__") and not k in exclude}
    
    text = replaceAll(text, settings)

    with open(template_file.split(".")[0] + ".html", "w") as f:
        f.write(text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Correct usage: python3 render.py <FILENAME>.template")
        exit()
    main(sys.argv[1])