import os
import scrap

from trello import TrelloClient
from markdownify import markdownify as md

client = TrelloClient(
    api_key=os.getenv('TRELLO_API_KEY'),
    api_secret=os.getenv('TRELLO_API_SECRET'),
)


all_boards = client.list_boards()
target_board = None
for board in all_boards:
    if board.name == os.getenv('PROJECT_NAME'):
        target_board = board
        break

if target_board is None:
    raise Exception("Target board not found")


target_list = None
for tlist in target_board.list_lists():
    if tlist.name == 'New':
        target_list = tlist
if not target_list:
    target_list = target_board.add_list('New')


previously_added_list = []

if os.path.exists('added_projects'):
    with open('added_projects') as f:
        previously_added_list.extend([x.strip() for x in f.readlines() if x.strip()])


def add_proj(proj):
    detail_resp, link = scrap.get_project_detail(proj['id'])

    proposer = proj['proposer']['name']
    tags = ' #'.join(proj['tags'])
    difficulty = detail_resp['difficulty']

    title = f'{difficulty} - {proj["title"]} - {proposer}'

    desirable = detail_resp.get('additional', {}).get('desirable-skills', '')
    essentials = detail_resp.get('additional', {}).get('essential-skills', '')

    desc_md = md(detail_resp['description'])

    content = f"""
## tags
{tags}

## Link
{link}

# Difficulty
{detail_resp["difficulty"]}


# Description
{desc_md}

# Goal
{detail_resp["goal"]}

# Completion
{detail_resp["completion"]}

# Skills

## Essentials

{essentials}

## Desirable

{desirable}
    """

    target_list.add_card(
        name=title,
        desc=content
    )


for proj in scrap.get_project_list():
    if str(proj['id']) in previously_added_list:
        continue

    try:
        add_proj(proj)
        previously_added_list.append(str(proj['id']))
    except Exception as e:
        print(proj['id'])
        print(e)

with open('added_projects', 'w') as f:
    f.write('\n'.join(previously_added_list))
