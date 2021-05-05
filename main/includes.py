import pandas as pd
import numpy as np
import os


class Includes :
    def getDays(self) :
        path = os.path.abspath(os.path.dirname(__file__))
        dataset = pd.read_csv(path+'\weatherHistory.csv')
        final_summary = pd.DataFrame(dataset)
        unique_values = final_summary.Summary.unique()
        final_summary.Summary = pd.Categorical(final_summary.Summary)
        final_summary['summary_code'] = final_summary.Summary
        final_summary['Summary'] = final_summary.Summary.cat.codes
        final_precip_type = pd.DataFrame(dataset)
        unique_values_precip_types = final_precip_type['Precip Type'].unique()
        final_precip_type['Precip Type'] = pd.Categorical(final_precip_type['Precip Type'])
        final_precip_type['precip_type'] = final_precip_type['Precip Type']
        final_precip_type['Precip Type'] = final_precip_type['Precip Type'].cat.codes
        tempreature_training_set = final_precip_type.iloc[:,1:11]

        tempreature_training_set = np.array(tempreature_training_set)
        return tempreature_training_set[:, 0:11]