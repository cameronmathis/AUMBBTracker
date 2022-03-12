import constants.services
from services.DaysSinceLoss import main as daysSinceLoss
import sys
import logging
# for file logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='AUMBBTracker.log', force=True, level=logging.INFO)


# Main method to run the application
def main():
    serviceToRun = ""
    if len(sys.argv) == 2:
        serviceToRun = sys.argv[1]
    else:
        logging.error(
            f"No service argument passed.")
        quit()

    if serviceToRun == constants.services.DAYS_SINCE_LOSS:
        logging.info(
            f"Calling service: {serviceToRun}.")
        daysSinceLoss()
    elif serviceToRun == constants.services.DAYS_TILL_GAME:
        logging.error(
            f"Service not operational.")
    else:
        logging.error(
            f"Service not found.")
        quit()


        # call the main method
if __name__ == "__main__":
    main()
