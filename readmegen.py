# README Generator for Unity Project

# Import the required modules
import os
from AICaller import *

# Set the project directory as the current directory
project_directory = os.getcwd()

# Create an empty list to store the sections of the README
sections = []

# Define the brief description of the Unity scripts in the repository and append it to the list
title = input(f"Please add Repository Title: \n")
user_desc =  input(f"Please provide a brief description of your repository: \n")
description = f'<h1 align="center"> {title} <h1> \n\n {gpt3_completion((open_file("openai_prompts/description.txt")).replace("<<PROMPT>>",user_desc) , 0.5)}'
sections.append(description)

def get_file_extensions(directory):
    extensions = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            extensions.add(ext)
    return extensions

# Define the technologies used in the Unity project
technologies = ['\n\n## Technologies Used\n']
tech_set = {x.strip() for x in gpt3_completion((open_file("openai_prompts/technologies.txt")).replace("<<PROMPT>>", description), 0).split((", ")[:-1])}
extensions = get_file_extensions(project_directory)
extensions_dict = { '.js': 'JavaScript', '.py': 'Python', '.java': 'Java', '.cpp': 'C++', '.c': 'C', '.h': 'C Header', '.cs': 'C#', '.rb': 'Ruby', '.php': 'PHP', '.html': 'HTML', '.css': 'CSS', '.json': 'JSON', '.xml': 'XML', '.sql': 'SQL', '.kt': 'Kotlin', '.swift': 'Swift', '.go': 'Go', '.m': 'Objective-C', '.sh': 'Bash', '.ps1': 'PowerShell', '.ts': 'TypeScript', '.scss': 'Sass', '.less': 'Less', '.md': 'Markdown', '.yaml': 'YAML', '.csv': 'CSV', '.log': 'Log', '.odt': 'ODT', '.pdf': 'PDF', '.doc': 'DOC', '.docx': 'DOCX', '.xls': 'XLS', '.xlsx': 'XLSX', '.ppt': 'PPT', '.pptx': 'PPTX', '.bmp': 'BMP', '.gif': 'GIF', '.jpg': 'JPG', '.jpeg': 'JPEG', '.png': 'PNG', '.svg': 'SVG', '.yml': 'YAML', '.mdx': 'MDX', '.jsx': 'JSX', '.tsx': 'TSX', '.vue': 'Vue.js', '.jsx': 'React', '.tsx': 'React', '.vue': 'Vue.js', '.svelte': 'Svelte', '.dart': 'Dart', '.rs': 'Rust', '.asm': 'Assembly', '.pl': 'Perl', '.hs': 'Haskell', '.swift': 'Swift', '.groovy': 'Groovy', '.lua': 'Lua', '.scala': 'Scala', '.coffee': 'CoffeeScript', '.elm': 'Elm', '.jl': 'Julia', '.tf': 'Terraform', '.tfvars': 'Terraform', '.terraform': 'Terraform', '.tfstate': 'Terraform', '.tfstate.backup': 'Terraform', '.pug': 'Pug', '.ejs': 'EJS', '.twig': 'Twig', '.hbs': 'Handlebars', '.haml': 'Haml', '.slim': 'Slim', '.cfm': 'ColdFusion', '.lua': 'Lua', '.gradle': 'Gradle', '.r': 'R', '.d': 'D', '.tex': 'LaTeX', '.bib': 'BibTeX', '.makefile': 'Makefile', '.cmake': 'CMake', '.am': 'Automake', '.ac': 'Autoconf', '.patch': 'Patch', '.diff': 'Diff', '.sql': 'PL/SQL', '.scpt': 'AppleScript', '.applescript': 'AppleScript'}
for ext in extensions:
    if extensions_dict.get(ext) :
        tech_set.add(extensions_dict.get(ext))
for tech in tech_set:
    technologies.append(f'- {tech}\n')
sections.append('\n'.join(technologies))

# Define a how-to-use section for the Unity project and append it to the list
# divide in several possibilities
#
how_to_use =  '''\n## How to Use

1. Clone the repository.
2. Open the command line and navigate to the cloned repository.
3. Add you OpenAI API key to AICaller.py.
4. Run the `readme_generator.py` script.
5. The README file will be generated in the same directory as the script.
6. Still a work in progress, but rn you can grasp the general idea.
7. Check you readme througly, This OpenAi model is NOT finetunned, tends to hallucinate.
'''
sections.append(how_to_use)

# Define the index of useful coding resources and append it to the list

Resources = f'\n## Index of Useful Resources\n\n {gpt3_completion((open_file("openai_prompts/resources.txt")).replace("<<PROMPT>>", description), 0)}'

sections.append(Resources)

# Define any technical considerations that are important for the Unity project and append it to the list
#considerations = '''## Technical Considerations
#- This project was developed using Python version X.X.X.
#- The generated README file is in Markdown format.
#'''
#sections.append(considerations)


# Define a references section for the Unity project and append it to the list
#references = '''## References
#- [Markdown Guide](https://www.markdownguide.org/)
#- [Python Official Documentation](https://docs.python.org/)
#- [PyInquirer Documentation](https://github.com/CITGuru/PyInquirer)
#'''
#sections.append(references)

# Define an author section for the Unity project and append it to the list
author = '\n\n## Author\n\n'

# Define information types
info_types = ["Name", "Job Title", "Location", "Email", "Phone", "Webpage"]

# Generate questions dynamically
for info_type in info_types:
    while True:
        response = input(f"Do you want to add your {info_type}? (y/n) ")
        if response.lower() == "y":
            info = input(f"{info_type}: ")
            author += f"{info_type}: {info}\n"
            break
        elif response.lower() == "n":
            break
        else:
            print("Please enter y or n.")

#author = '''## Author
#Manuel Alejandro Grau Bastidas
#Desarrollador de Software - Comunidad de Madrid - España
#E-mail: manuelgb94@gmail.com
#Teléfono: +34 676 18 02 00
#https://www.linkedin.com/in/manuel-grau-bastidas/
#'''
if author != '\n\n## Author\n\n':
    sections.append(author)

# Define the filename for the README
filename = 'README.md'

# Create the README
with open(os.path.join(project_directory, filename), 'w', encoding='utf-8') as f:
    for section in sections:
        f.write(section)
