import json

# data.json is in JSON converted from semantic scholar, replace '=' with ':'
acm_data = json.load(open('./data.json', "r"))


# Get authors name in required format only takes first and last name, does not consider middle names.
def get_author(author):
    temp = author.split(',')
    temp = [x.replace(" ", "") for x in temp]
    return temp[-1][:1]+". "+temp[0]

for ref in acm_data:
    cite = ref['0']
    author = ''
    for aut in ref['author'].split('and'):
        author = author + get_author(aut) +", "

    title = ref['title']
    if 'booktitle' in ref:
        conf = ref['booktitle']
    elif 'journal' in ref:
        conf = ref['journal']
    elif 'publisher' in ref:
        conf = ref['publisher']
    year = ref['year']
    print "\\bibitem{"+cite+"} "+ author + "``"+title+",'' " + conf + ", " + year +"."


