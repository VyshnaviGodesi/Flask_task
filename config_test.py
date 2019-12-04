from configparser import ConfigParser


def read_db_config(filename='dev.ini'):
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section('sql_config'):
        db['Driver'] = parser.get('sql_config', 'Driver')
        db['Server'] = parser.get('sql_config', 'Server')
        db['Database'] = parser.get('sql_config', 'Database')
        db['username'] = parser.get('sql_config', 'username')
        db['password'] = parser.get('sql_config', 'password')
        print(db)
    else:
        raise Exception('{0} not found in the {1} file'.format('sql_config', filename))

    return db
read_db_config();

