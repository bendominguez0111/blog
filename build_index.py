"""
Builds the index page based off posts in the posts folder.
"""
import os

files = os.listdir("_posts")

host = 'https://bendominguez011.github.io/blog'

with open('README.md', 'w') as readme:
    readme.write('# Blog Posts\n\n')
    for file in files:
        year = file.split('-')[0]
        month = file.split('-')[1]
        day = file.split('-')[2]
        title = '-'.join(file.split('-')[3:]).split('.')[0]
        readme.write(f'[{year}-{month}-{day} - {title}]({host}/{year}/{month}/{day}/{title}.html)\n\n')
