from logger import logger_init

class Tester:
    def tester(self,func,tests):
        for count, test in enumerate(tests):
            if func(test[0]) == test[1]:
                logger.info(f"{count}. Test Passed")
            else:
                logger.error("Failed: {} insted of: {}".format(func(test[0], test[1]), test[2]))

logger = logger_init()