import datetime
class Logger:

    def __init__(self):
        self.file_name = 'logs.txt'

    def write_logs(self, func_name, err=None):
        with open(self.file_name, 'a') as log_file:
            log_file.write("FUNCTION: %s\n" % func_name)
            cur_time = datetime.datetime.now()
            log_file.write("ERROR: %s\n" % err)
            log_file.write("TIME: %s\n" % cur_time)
            log_file.write("END FUNCTION\n")
            log_file.write("\n")

