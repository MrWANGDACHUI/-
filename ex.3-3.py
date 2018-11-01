dayup, dayfactor = 1.0, 0.01
for i in range(1,366):
    if i % 10 in [4,5,6,7]:
        dayup = dayup * (1 + dayfactor)
    print("{}：天的能力{}".format(i+1,dayup))
print("连续学习3天能力值不变，从第4天至第7天每天能力增长为前一天1%，每10天休息一天的力量: {:.2f}.".format(dayup))
