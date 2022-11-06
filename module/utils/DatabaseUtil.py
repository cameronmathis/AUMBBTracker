import logging
import shelve

DATABASE = "database"


# Gets the most previous record from database
# Returns:
#   a string
def getRecord():
    try:
        db = shelve.open(DATABASE)
        record = db["record"]
        db.close()
        logging.info(
            f"Successfully retrieved the record from the database. | Record: {record}")
        return record
    except KeyError:
        record = "0-0"
        db["record"] = record
        db.close()
        logging.info(
            f"No record stored in the database. Initialed to {record}.")
        return record


# Stores the current record in database
# Parameters:
#     record - a string indicating the record to be stored in the database
def setRecord(record):
    db = shelve.open(DATABASE)
    db["record"] = record
    db.close()
    logging.info(
        f"Successfully stored the record in the database. | Record: {record}")


# Gets the number of days since a loss from database
# Returns:
#   a string
def getLastLossDate():
    try:
        db = shelve.open(DATABASE)
        lastLossDate = db["lastLossDate"]
        db.close()
        logging.info(
            f"Successfully retrieved the last loss date from the database. | Last Loss Date: {lastLossDate}")
        return lastLossDate
    except KeyError:
        db.close()
        lastLossDate = "01/01/1900"
        setLastLossDate(lastLossDate)
        logging.info(
            f"No last loss date in the database. Initialed to {lastLossDate}.")
        return lastLossDate


# Stores the number of days since a loss in database
# Parameters:
#     lastLossDate - a string indicating the last lost date to be stored in the database
def setLastLossDate(lastLossDate):
    db = shelve.open(DATABASE)
    db["lastLossDate"] = lastLossDate
    db.close()
    logging.info(
        f"Successfully stored the last loss date in the database. | Last Loss Date: {lastLossDate}")
