class BatchSettings:
    batch_size = 0

    def read_settings_file(self):
        f = open('../DataCollector/batch_settings.txt', 'r')

        for line in f:
            if 'batch_size=' in line:
                cleaned_line = line.replace('batch_size=', '')
                self.batch_size = int(cleaned_line)
