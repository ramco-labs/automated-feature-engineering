import pandas as pd


class EntityGeneration:
    @staticmethod
    def entity_segregation(df, outputs):
        entities = []
        unique_index = [index for index in range(len(df))]
        for output in outputs:
            new_df = pd.DataFrame(df[output], columns=[output])
            new_df['index'] = unique_index
            entities.append(new_df)
            df.drop(output, axis=1, inplace=True)
        df['index'] = unique_index
        entities.append(df)
        return entities
