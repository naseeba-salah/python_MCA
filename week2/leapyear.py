year1=int(input("enter the starting year"))
year2=int(input("enter the end year"))
for year in range(year1,year2+1):
    if((year%100==0)or( year%4==0))and((year%100!=0)or(year%400==0)):
        print(year)
