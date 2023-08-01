from collection import Collection

raw = [{'name': 'istambul', 'country': 'turkey'},
       {'name': 'Moscow ', 'country': ' Russia'},
       {'name': 'iStambul', 'country': 'tUrkey'},
       {'name': 'antalia', 'country': 'turkeY '},
       {'name': 'samarA', 'country': '  ruSsiA'}]



def format(raw):
    new_raw = raw

    for i in new_raw:
        i.update({'name': i['name'].lower().strip(), 'country': i['country'].lower().strip()})
    #return new_raw

    c = Collection(new_raw)

    #c.unique().group_by(lambda row: (row['country'], row['name'])).sort_by(lambda row: list(row.keys())).all()

    return c.unique().group_by(lambda row: (row['country'], row['name'])).sort_by(lambda row: list(row.keys())).all()



print(format(raw))