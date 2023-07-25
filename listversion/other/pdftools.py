import pandas as pd


# turns a list of two tuples to dataframe with 

def createDF(theList):
    df = pdf = pd.DataFrame(data_list, columns=['ages', 'rates'])
    df.to_csv('data.csv', index=False)
    return df


def createcsv(theList):
    with open('data.csv', 'w', newline='') as csvfile:
         csvwriter = csv.writer(csvfile)
         csvwriter.writerow(['ages', 'rates'])  # Write the header row
         csvwriter.writerows(data_list)



# remove outliers (outside of ? many standard deviations)
