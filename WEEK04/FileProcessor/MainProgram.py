import data_processor as dp

class MainProgram:

    def main():

        # load csv file data
        csv_file_path = 'D:\\ASSINGMENTS\\MSE800\\Activities\\WEEK04\\FileProcessor\\Data\\sample_junk_mail.csv'       
        processor = dp.DataProcessor(csv_file_path)
        processor.load_data()
        processor.initial_processing()

        # load parquet file data
        csv_file_path = 'D:\\ASSINGMENTS\\MSE800\\Activities\\WEEK04\\FileProcessor\\Data\\Sample_data_2.parquet'       
        processor = dp.DataProcessor(csv_file_path)
        processor.load_data()
        processor.initial_processing()

        # load csv file data
        csv_file_path = 'D:\\ASSINGMENTS\\MSE800\\Activities\\WEEK04\\FileProcessor\\Data\\sample_junk_mail.csv'       
        processor = dp.DataProcessor(csv_file_path)
        processor.load_data()
        processor.initial_processing()

    if __name__ == "__main__":
        main()
