import shelve

'''
Gets the most previous record from database

Returns a string
'''


def getRecord():
    db = shelve.open("database")
    record = db["record"]
    db.close()

    return record


'''
Stores the current record in database
'''


def setRecord(record):
    db = shelve.open("database")
    db["record"] = record
    db.close()

    return


'''
Gets the number of days since a loss from database

Returns a string
'''


def getLastLossDate():
    db = shelve.open("database")
    lastLostDate = db["lastLossDate"]
    db.close()

    return lastLostDate


'''
Stores the number of days since a loss in database
'''


def setLastLossDate(lastLostDate):
    db = shelve.open("database")
    db["lastLossDate"] = lastLostDate
    db.close()

    return
