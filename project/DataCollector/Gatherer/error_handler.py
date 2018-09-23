import datetime
import io


class ErrorHandler:
    log = []

    def add_to_log(self, username, status):
        current = datetime.datetime.now()
        log_error = self.get_status(status) + '@' + username + '#' + current.strftime('%H-%M-%S--%m-%d-%Y--%A')
        self.log.append(log_error)

    def write_log_file(self):
        time = self.calculate_current_time()
        with io.open('../Data/error/errors-%s.txt' % time, 'a', encoding='utf8') as outfile:
            if len(self.log) == 0:
                outfile.write('No errors.')
            else:
                for error in self.log:
                    outfile.write('%s\n' % error)

    def calculate_current_time(self):
        current = datetime.datetime.now().strftime('%H-%M-%S--%m-%d-%Y--%A')
        return current

    def get_status(self, status):
        if status == 1:
            return 'ON-RECEIVING-FROM-API'

        return 0
