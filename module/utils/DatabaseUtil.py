import shelve

db = "database"


# Gets the most previous record from database
# Returns:
#   a string
def getRecord():
    try:
        db = shelve.open(db)
        record = db["record"]
        db.close()
        return record
    except KeyError:
        db.close()
        record = "0-0"
        setRecord(record)
        return record


# Stores the current record in database
# Parameters:
#     record - a string indicating the record to be stored in the database
def setRecord(record):
    db = shelve.open(db)
    db["record"] = record
    db.close()


# Gets the number of days since a loss from database
# Returns:
#   a string
def getLastLossDate():
    try:
        db = shelve.open(db)
        lastLostDate = db["lastLossDate"]
        db.close()
        return lastLostDate
    except KeyError:
        db.close()
        lastLostDate = "01/01/1900"
        setLastLossDate(lastLostDate)
        return lastLostDate


# Stores the number of days since a loss in database
# Parameters:
#     lastLostDate - a string indicating the last lost date to be stored in the database
def setLastLossDate(lastLostDate):
    db = shelve.open(db)
    db["lastLossDate"] = lastLostDate
    db.close()
