"""
Builds the index page based off posts in the posts folder.
"""
import os

files = os.listdir("_posts")

with open('README.md', 'w') as readme:
    readme.write('# Blog Posts\n\n')
    for file in files:
        readme.write(f'* [{file[:-3]}]({file})\n')