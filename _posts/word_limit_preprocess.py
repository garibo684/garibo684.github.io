import os
import re

word_limit = 80  # Set your desired word limit per line

content_directory = "/home/garibo684/projects/garibo684.github.io/_posts/"  # Update with the actual path to your content directory

# Traverse through all Markdown files in the content directory
for root, dirs, files in os.walk(content_directory):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            
            # Read the contents of the Markdown file
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Apply the word limit logic using regular expressions
            modified_content = re.sub(r'(\S+\s+){%d}' % word_limit, r'\g<0>\n', content)
            
            # Write the modified content back to the Markdown file
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(modified_content)
