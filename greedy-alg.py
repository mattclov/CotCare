# patients  = ["Patient Code", Latest Treating Time, Estimated Completion Time]

patients = [["P1", 0, 2],
              ["P2", 3, 5],
              ["P3", 1, 8],
              ["P4", 5, 8],
              ["P5", 5, 7],
              ["P6", 8, 9]
                ]

#Function: patient selection
def printMaxPatients(patients):
    patients.sort(key=lambda x: x[2])
    i = 0
    firstA = patients[i][0]
    print(firstA)
    for j in range(len(patients)):
        if patients[j][1] > patients[i][2]:
            print(patients[j][0])
            i = j

printMaxPatients(patients)

# If the patient is not selected, he/she will be assigned to another cot