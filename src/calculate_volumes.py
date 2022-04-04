from os import listdir
from segmentation.measure import Measures
import sys

if __name__ == '__main__':
    if sys.argv[1]:
        patient_dict = {}
        for file in sorted(listdir(sys.argv[1])):
            if file.endswith('nii.gz'):
                patient = file.split('_')[0]
                if patient in patient_dict.keys():
                    patient_dict[patient].append(sys.argv[1]+'/'+file)
                else:
                    patient_dict[patient] = [sys.argv[1]+'/'+file]

        for patient in patient_dict.keys():
            measure: Measures = Measures()
            print(patient)
            print("--------------------------------------------")
            measure.calculate_volume(patient_dict[patient], 0)
