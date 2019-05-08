import pandas as pd


class UserInput:
    @staticmethod
    def input_process(path, uid, outputs):
        try:
            df = pd.read_csv(path)
            for output in outputs:
                try:
                    keys = list(df.keys())
                    keys.index(output)
                except ValueError:
                    print("error key not found :", output)
            return df, uid, outputs
        except IOError:
            print("File not found", path)


#user_input = UserInput()
#print(user_input.input_process("../data/autocoding_aviation-autocoding.csv", "1234", ['test', 'fb_id']))
