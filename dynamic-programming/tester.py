from logger import logger_init

class Tester:
    def tester(self,func,tests):
        logger = logger_init()
        for count, test in enumerate(tests):
            # if func(test[0],test[1]) == test[-1]:
            func_output = func(test[0])
            if func_output == test[-1]:
                logger.info(f"{count}. Test Passed")
            else:
                # logger.error("Failed: {} insted of: {}".format(func(test[0],test[1]), test[-1]))
                logger.error("Failed: {} insted of: {}".format(func_output, test[-1]))