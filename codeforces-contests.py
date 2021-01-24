import codeforces_api
import os

cf_api = codeforces_api.CodeforcesApi(
    os.environ['CODEFORCES_API_KEY'],
    os.environ['CODEFORCES_API_SECRET']
)

handles = [
    'Periquito',
    'milanesita',
    'iglosiggio',
    'Heibor',
    'reedef',
    'Agua_Podrida',
    'pejerrey',
    'stringa',
    'Mateo',
    'Radeon123',
    'tsukareru',
    'maidaneze',
    'eiff',
    'Zhaere',
    'facuruiz',
    'Guty',
    'pache_n',
]

div = 2


def is_finished_div_2(contest):
    return f'Div. {div}' in contest['name'] and contest['phase'] == 'FINISHED'


def get_contest_id(contest):
    return contest['id']


def request_standings(contest):
    return cf_api.contest_standings(
        contest_id=contest['id'],
        handles=handles,
        show_unofficial=True
    )['result']


def get_member_of_row(row):
    return row['party']['members'][0]['handle']


def print_found_contest(contest):
    contest_id = contest['id']
    standings_url = 'https://codeforces.com/contest/{}/standings/friends/true'\
        .format(contest_id)
    virtual_url = 'https://codeforces.com/contestRegistration/{}/virtual/true'\
        .format(contest_id)
    print('================')
    print('Found contest!')
    print('Name:', contest['name'])
    total_minutes = contest['durationSeconds'] / 60
    print('Duration:',  '{}:{:02d}'.format(int(total_minutes // 60), int(total_minutes % 60)))
    print('Standings:', standings_url)
    print('Virtual participation:', virtual_url)
    print('================')


contests = cf_api.contest_list()['result']
div2_contests = filter(is_finished_div_2, contests)
sorted_contests = sorted(div2_contests, key=get_contest_id, reverse=True)
standings = map(request_standings, sorted_contests)
for standing in standings:
    print('Checking', standing['contest']['id'], '...')
    rows = standing['rows']
    if not rows:
        contest = standing['contest']
        print_found_contest(contest)

