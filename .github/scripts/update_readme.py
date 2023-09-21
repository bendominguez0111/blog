"""
Builds the index page based off posts in the posts folder.
"""
import os

files = os.listdir("_posts")

host = 'https://bendominguez0111.github.io/blog'

with open('README.md', 'w') as readme:
    readme.write('### Posts:\n\n')
    for file in files:
        year = file.split('-')[0]
        month = file.split('-')[1]
        day = file.split('-')[2]
        post_url = '-'.join(file.split('-')[3:]).split('.')[0]
        with open('_posts/' + file, 'r') as post:
            # grab the third line of the post, which is the title
            title = post.readlines()[2].split(':')[-1].lstrip()
        readme.write(f'[{title} - ({year}.{month}.{day})]({host}/{year}/{month}/{day}/{post_url}.html)\n\n')
