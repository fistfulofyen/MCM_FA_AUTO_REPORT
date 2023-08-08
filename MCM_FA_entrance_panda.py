import pandas as pd

#path = r"C:\Users\zhang\Downloads\MCM_FA_DASHBOARD_WMELD_ALL_2777 (2).csv"
# or use '/'
data = pd.read_csv("C:\\Users\\zhang\\Downloads\\MCM_FA_DASHBOARD_WMELD_ALL_2777 (2).csv")

'''
1. Filter by MATR/DEIN
2. remove duplicates - eliminate by eval number, keep highest evaluation number
3. Find all UHMML academic program and change the faculty field to match appropriate academic plan
        All UHMML are attached to Humanities Faculties ex) Engineering MELD will indicate Humanities academic program, 
        need to change academic pgm column to UENDG
4. only include NURS_MCM, other program are not eligable for entrance awards

Faculty	Plan

6.
find the total number of student matr for 
A$S/93+, Business/90+, Engineering/95+, Health_Science/94+, Humanities/90+, Science/94+, Social_Sciences/90+

2022-2023 Estimated Top 10% Admission Averages for 
A$S/98.5, Business/95.33, Engineering/97.4, Health_Science/99, Humanities/95, Science/97.5, Social_Sciences/94.66

saparate each by international vs Domestic

'''
#step 2
#data = data.sort_values('Eval Nbr').drop_duplicates('Appl Nbr',keep = 'last')

#step 3

# acad_prog = {
#     ['MBUSINESS1'] :'Business',
#     ["'MBTECH_AV1', 'MBTECH_BI1','MBTECH_PA1','MCOMPSCCO1','MCOMPSCI1','MENGINEER1'"]: 'Engineering',
#     ["'MHUM1','MMUSIC'"]: 'Humanities',
#     ["'MENVEARTH1','MLIFESCI1','MMATHSTAT1','MPHYSSC1'"]:'Science',
#     ["'MECONMICS1','MHLTHSCTY1','MSOCSCI1'"]:'Social Sciences',
# }
# if data.loc['Acad Prog'] == 'UHMML':
#     if data.loc[acad_prog[None]]:
#         pass

#step 6

header = data.columns
faculty_list = data['Faculty'].unique().tolist()
faculty_list.sort()
stu_matr_crti = {
    'Arts & Science' : 93,
    'Business' : 90,
    'Engineering' : 95,
    'Health Sciences' : 94,
    'Humanities' : 90,
    'Science': 94,
    'Social Sciences' : 90
}
stu_top10_crti = {
    'Arts & Science' : 98.5,
    'Business' : 95.33,
    'Engineering' : 97.4,
    'Health Sciences' : 99,
    'Humanities' : 95,
    'Science': 97.5,
    'Social Sciences' : 94.66,
}

matr = []
matr_D_I = []

eligible = []
eligible_D_I = []

top10 = []
top10_D_I = []
# & means and, | means or
for faculty in faculty_list:

    matrulated = (data['Faculty'] == faculty) & (data['Prog Actn'] == 'MATR' )

    temp = (data.loc[matrulated]).shape[0]
    matr.append(temp)
    temp_D_I = (data.loc[matrulated & (data['Status'] != '4')]).shape[0]
    matr_D_I.append([temp_D_I, temp - temp_D_I])

    temp = (data.loc[matrulated & (data['Value'] >= stu_matr_crti[faculty])]).shape[0]
    eligible.append(temp)
    temp_D_I = (data.loc[matrulated & (data['Value'] >= stu_matr_crti[faculty]) & (data['Status'] != '4')]).shape[0]
    eligible_D_I.append([temp_D_I, temp - temp_D_I])

    temp = (data.loc[matrulated & (data['Value'] >= stu_top10_crti[faculty])]).shape[0]
    top10.append(temp)
    temp_D_I = (data.loc[matrulated & (data['Value'] >= stu_top10_crti[faculty]) & (data['Status'] != '4')]).shape[0]
    top10_D_I.append([temp_D_I, temp - temp_D_I])

print(faculty_list)
print(matr,'\n',matr_D_I)
print(eligible,'\n',eligible_D_I)
print(top10,'\n',top10_D_I)

