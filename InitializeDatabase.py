import shelve

'''
Initializes the database
    
Parameters: 
    record - the record
    lastLostDate - the last lost date
'''


def initializeDatabase(record, lastLostDate):
    db = shelve.open("database")
    db["record"] = record
    db["lastLossDate"] = lastLostDate
    db.close()

    return


'''
Prints the values in database
'''


def checkDatabase():
    db = shelve.open("database")
    print(db["record"])
    print(db["lastLossDate"])
    db.close()

    return


initializeDatabase("0-0", "01/01/2000")

# checkDatabase()
