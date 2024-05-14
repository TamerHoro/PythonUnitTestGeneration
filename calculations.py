# hc_coverage_values = [
#     56.0, 72.0, 76.0, 72.0, 75.0, 67.0, 62.0, 59.0, 64.0, 61.0,
#     82.0, 66.0, 72.0, 67.0, 53.0, 71.0, 63.0, 64.0, 69.0, 74.0
# ]

# hc_average_coverage = sum(hc_coverage_values) / len(hc_coverage_values)
# print(hc_average_coverage)


# an_coverage_values = [
#     77.0, 63.0, 72.0, 73.0, 69.0, 69.0, 71.0, 65.0, 71.0, 74.0,
#     58.0, 79.0, 71.0, 69.0, 72.0, 76.0, 75.0, 65.0, 67.0, 74.0
# ]

# an_average_coverage = sum(an_coverage_values) / len(an_coverage_values)
# print(an_average_coverage)

#Default
# covVal1 = [41.0, 51.0, 42.0, 51.0, 45.0, 53.0, 59.0, 60.0, 44.0, 57.0, 39.0, 42.0, 53.0, 51.0, 58.0, 54.0, 51.0, 45.0, 56.0, 57.0]
# timeP1 = [10.48, 15.15, 13.00, 11.08, 12.66, 21.97, 18.66, 14.51, 15.72, 13.33, 13.62, 11.48, 13.01, 17.04, 17.95, 13.60, 16.70, 13.33, 19.60, 12.06]

# avCov1= sum(covVal1)/len(covVal1)
# avT1 = sum(timeP1)/len(timeP1)

# print("avCov: "+ str(avCov1))
# print("avTime: "+ str(avT1))

# #CN
# covVal2 = [31.0, 44.0, 40.0, 61.0, 44.0, 46.0, 35.0, 43.0, 52.0, 55.0, 56.0, 63.0, 44.0,51.0, 54.0, 57.0, 50.0, 45.0, 51.0, 59.0]
# timeP2= [27.39, 12.48, 56.45, 46.22, 37.63, 12.41, 10.82, 11.35, 39.77, 44.13, 47.90, 43.23, 11.10, 42.85, 44.57, 43.59, 53.93, 40.49, 43.51, 51.22 ]


# avCov2= sum(covVal2)/len(covVal2)
# avT2 = sum(timeP2)/len(timeP2)

# print("avCov: "+ str(avCov2))
# print("avTime: "+ str(avT2))

#Acceptance rate avarage

accRates = [-1, -1, 0.0, 0.5, 0.75, 0.75, 0.5]

avAcc= sum(accRates)/len(accRates)


print("avAcc: "+ str(avAcc))
