

##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################

df = sns.load_dataset("titanic")
#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################

df.head()
df["sex"].value_counts()

#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################
df.nunique()



#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################

df["pclass"].unique()


#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################
df[["pclass","parch"]].nunique()


#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################

df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype
#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################

df[df["embarked"] == "C"]

#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################

df[df["embarked"] != "S"]

#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################

df[(df["age"] < 30) & (df["sex"] == "female")]

#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################

df[(df["fare"] > 500) | (df["age"] > 70)]


#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################

df.isnull().sum()

#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################
df.drop("who", axis=1).head()
df.head()

#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################

df["deck"].fillna(df["deck"].mode().iloc[0], inplace=True)
df["deck"].isnull().sum()  # 0 olmalı ✅

df.head()

#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################
df["age"].fillna(df["age"].median(), inplace=True)
df["age"].isnull().sum()  # 0 olmalı ✅
df["age"].median()      # medyan değerini görmek için
df["age"].head()
# Bonus bilgi
df["survived"].dtype
df["survived"]=df["survived"].map({0:"No",1:"Yes"})
df.head()
df_csv =df("titanic",index=False)

#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################
df.groupby(["pclass"]).agg({"age":"mean"})
df.groupby(["pclass","sex"]).agg({"survived": ["sum","count","mean"]})
df.groupby(["sex","pclass"]).agg({"survived": ["sum","count","mean"]})

#### **************
stats = ['sum', 'count', 'mean']
grouped_data = df.groupby(['pclass', 'sex'])['survived'].agg(stats)

grouped_data.columns = [f"survived_{stat}" for stat in stats]
grouped_data.columns
grouped_data.head()
grouped_data = pd.DataFrame(grouped_data).reset_index()
grouped_data.head()

#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################

df.head()

df["age_flag"] = df["age"].apply(lambda x: 1 if x<30 else 0)
def age_classifier(age):
    return 1 if age < 30 else 0


df["age_flag_2"] = df["age"].apply(lambda x: age_classifier(x))
df.head()



# Sonuçları kontrol edelim
df[['age', 'age_flag']].head() ## *********

#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################

df = sns.load_dataset("tips")
df.head()
df.shape


#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################
df.groupby("time").agg({"total_bill" : ["sum","min","max","mean"]})



#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################
df.groupby(["time","day"]).agg({"total_bill" : ["sum", "min","max","mean"]})
df.groupby(["day","time"]).agg({"total_bill" : ["sum", "min","max","mean"]})



#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################

(df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({
    "total_bill": ["sum", "min", "max", "mean"],
    "tip": ["sum", "min", "max", "mean"],
    "size": "mean"}))

#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################

df.loc[(df["size"] < 3) & (df["total_bill"] > 10), ["total_bill"]].mean()
# Bonus
df[(df["size"] < 3) & (df["total_bill"] > 10)].mean(numeric_only=True)

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################
df.info()
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()
df2 = df["total_bill_tip_sum"].sort_values(ascending = False).head(30).reset_index(drop = True)
df2.head()
#Bonus
top_30 = df.sort_values("total_bill_tip_sum", ascending=False).head(30)
top_30


#  BONUS: Total_bill değişkeninin kadın ve erkek için ayrı ayrı ortalamasını bulun.
# Bulduğunuz ortalamaların altında olanlara 0, üstünde ve eşit olanlara bir verildiği yeni bir total_bill_flag değişkeni oluşturun.
# Dikkat !! Female olanlar için kadınlar için bulunan ortalama dikkate alıncak, male için ise erkekler için bulunan ortalama.
# parametre olarak cinsiyet ve total_bill alan bir fonksiyon yazarak başlayın. (If-else koşulları içerecek)


f_avg = df[df["sex"]=="Female"]["total_bill"].mean() # 18.05
m_avg = df[df["sex"]=="Male"]["total_bill"].mean() # 20.74

def func (sex, total_bill):
    if sex == "Female":
        if total_bill >= f_avg :
            return 1
        else:
            return 0
    else:
        if total_bill >= m_avg:
            return 1
        else:
            return 0

df["total_bill_flag"] = df.apply(lambda x: func(x["sex"],x["total_bill"]), axis=1)
df.head(50)



#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################

temp_df = df.sort_values("total_bill_tip_sum")[:30]
temp_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
temp_df.head()


