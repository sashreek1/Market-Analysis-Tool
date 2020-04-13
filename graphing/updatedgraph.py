def get_plot(list1):
    from collections import Counter
    import pandas as pd
    import matplotlib.pyplot as plt
    
    list1 = [['04/10/2020, 18:00:39', 'mango', '43', 'farm', "{'orange': 0, 'yellow': 1, 'green': 0, 'red': 0, 'blue': 0}"], ['04/12/2020, 06:34:27', 'banana', '43', 'farm>dealer>supermarket', "{'red': 0, 'yellow': 3, 'green': 2, 'blue': 1, 'orange': 0}"]]
    
    age_list=[]
    age_list1=[]
    product_list=[]
    product_list1=[]
    path=[]
    path1=[]
    sales_and_age=[]
    sales_and_age1=[]
    
    
    for i in range(len(list1)):
        age_list.append(list1[i][2])
    age_list1= dict(Counter(age_list))
    df=pd.DataFrame(age_list1, index=['age '])
    df.plot(kind='bar')
    plt.savefig('output1.png')
    
    
    
    for i in range(len(list1)):
        product_list.append(list1[i][1])  
    product_list1= dict(Counter(product_list))
    df=pd.DataFrame(product_list1, index=['sold product'])
    df.plot(kind='bar')
    plt.savefig('output2.png')
    
    for i in range(len(list1)):
        path.append(list1[i][3])
    path1= dict(Counter(path))
    df=pd.DataFrame(path1, index=['path'])
    df.plot(kind='bar')
    plt.savefig('output3.png')
    
    for x in list1:
        temp1=x[1]
        temp2=x[2]
        temp3=temp1+temp2
        sales_and_age.append(temp3)
    sales_and_age1= dict(Counter(sales_and_age))
    df=pd.DataFrame(sales_and_age1, index=['sales vs age'])
    df.plot(kind='bar')
    plt.savefig('output4.png')
