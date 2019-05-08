import featuretools as ft
from input import UserInput
from entity_genration import EntityGeneration
import numpy as np


class FeatureGeneration:
    def __init__(self):
        self.es = ft.EntitySet()

    def entity_set(self, entity_list, outputs):
        t = 0
        entity_name = []
        for entity in entity_list:
            if t < len(output):
                entity_name.append(output[t])
                self.es = self.es.entity_from_dataframe(entity_id=outputs[t],
                                                        dataframe=entity,
                                                        index='index'
                                                        )
                t = t + 1
            elif t >= len(output):
                self.es = self.es.entity_from_dataframe(entity_id="features",
                                                        dataframe=entity,
                                                        index='index'
                                                        )
                entity_name.append("features")

        return entity_name

    def add_relationship(self, entity_list):
        for entity_name in entity_list:
            if entity_name != 'features':
                new_relationship = ft.Relationship(self.es["features"]["index"], self.es[entity_name]["index"])
                self.es = self.es.add_relationship(new_relationship)

    def generate_features(self, output_list):
        label_matrix_pair = {}
        for outputs in output_list:
            feature_matrix, feature_def = ft.dfs(entityset=self.es, target_entity=outputs)
            label_matrix_pair[outputs] = feature_matrix
        return label_matrix_pair


inp = UserInput()
ent = EntityGeneration()
fg = FeatureGeneration()
df, uid, output = inp.input_process("../data/autocoding_aviation-autocoding.csv", "1234", ['usage', 'fb_id'])
entities = ent.entity_segregation(df, output)
el1 = fg.entity_set(entities, output)
fg.add_relationship(el1)
print(fg.generate_features(output).keys())
