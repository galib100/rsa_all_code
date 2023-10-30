
# winners = [19728964, 30673077, 137289540, 195938621, 207242611, 237735979, 298141799, 302597011, 387047012, 405520686, 424852916, 461998372, 463977415, 528505766, 557896298, 603269308, 613528675, 621228168, 654758801, 670668388, 741571487, 753993381, 763314787, 770263388, 806543382, 864409584, 875042623, 875651556, 918697500, 946831967]
# fL =winners[:15]
# for i in range(0,16):
#     fL=winners[i:i+15]
#     print(fL)
#     if(sum(fL)==7627676296):
#         print("peyeci")
#         print(i)

# target = sum(winners)
# print(target)
# winners.sort()
# flag = "UDCTF{%s}" % (",".join(map(str,winners)))
# print(flag)
# choices.sort()
# print(choices)
# print(target)

from itertools import combinations

winners = [19728964, 30673077, 137289540, 195938621, 207242611, 237735979, 298141799, 302597011, 387047012, 405520686, 424852916, 461998372, 463977415, 528505766, 557896298, 603269308, 613528675, 621228168, 654758801, 670668388, 741571487, 753993381, 763314787, 770263388, 806543382, 864409584, 875042623, 875651556, 918697500, 946831967]

target_sum = 7627676296
num_to_select = 15

# Try all combinations of 15 numbers from the list
for combo in combinations(winners, num_to_select):
    if sum(combo) == target_sum:
        print("Found a combination that sums to the target:")
        print(combo)
        break
else:
    print("No combination of 15 numbers sums to the target.")
