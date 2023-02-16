# README Generator for Unity Project

# Import the required modules
import os

# Set the project directory as the current directory
project_directory = os.getcwd()

# Define the header section
header = f'# { os.path.basename(project_directory)}\n\n'

# Define the brief description of the Unity scripts in the repository
description = '''# README Generator

This is a fairly simple README generator that creates README files for explaining projects. It is written in Python and is currently a work in progress.

This repository contains a Python script for generating README files for your projects. The script takes user input to create various sections of a README, such as a project description, installation instructions, usage examples, and more. The goal of this project is to make it easy for developers to create high-quality README files for their projects.
'''

# Define the technologies used in the Unity project
technologies ='''## Technologies Used

- Python
'''

# Define any technical considerations that are important for the Unity project
considerations = '''## Technical Considerations

- This project was developed using Python version X.X.X.
- The generated README file is in Markdown format.
'''

# Define a how-to-use section for the Unity project
how_to_use =  '''## How to Use

1. Clone the repository.
2. Open the command line and navigate to the cloned repository.
3. Run the `readme_generator.py` script.
4. As of now its only a printer, but you wait i have a good idea on how to make a good decent one.
5. The README file will be generated in the same directory as the script.
'''
# Define the index of useful Unity coding resources
Resources = '''## Index of Useful README Resources

- [GitHub: Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- [A Beginners Guide to writing a Kickass README](https://meakaakka.medium.com/a-beginners-guide-to-writing-a-kickass-readme-7ac01da88ab3)
- [How to write a great README for your GitHub project](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
'''

# Define a references section for the Unity project
references = '''## References

- [Markdown Guide](https://www.markdownguide.org/)
- [Python Official Documentation](https://docs.python.org/)
- [PyInquirer Documentation](https://github.com/CITGuru/PyInquirer)
'''

# Define an author section for the Unity project
author = '''## Author

Manuel Alejandro Grau Bastidas
Desarrollador de Software - Comunidad de Madrid - España
E-mail: manuelgb94@gmail.com
Teléfono: +34 676 18 02 00
https://www.linkedin.com/in/manuel-grau-bastidas/
'''

# Define the filename for the README
filename = 'README.md'

# Create the README
with open(os.path.join(project_directory, filename), 'w') as f:
    f.write(header)
    f.write(description)
    f.write(technologies)
    f.write(considerations)
    f.write(how_to_use)
    f.write(Resources)
    f.write(references)
    f.write(author)
