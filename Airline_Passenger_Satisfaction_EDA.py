
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)


# GÖREV 1  ### Veri Seti Seçimi ###
df = pd.read_csv("/Users/iremkocagoz/Desktop/patikadev/archive/train.csv")


# GÖREV 2  ### İstatistiksel Özet ###
# Veri setindeki değişkenlere dair merkezi eğilim (ortalama, medyan vb.) ve dağılım (standart sapma, minimum, maksimum vb.) istatistikleri raporlanır.

#Görev 2.1  ### Veri seti ile ilgili genel bilgileri gösterme ###

df.info()       #103904 satır, 25 sütun
df.head()
df.index        #float64(1), int64(19), object(5)
df.describe().T
df.isnull().values.any()        #True
df.isnull().sum()               #Arrival Delay in Minutes - 310

#Görev 2.2  ### Sayısal Değişkenleri Belirleme ###
numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns
print("Sayısal Değişkenler:")
print(numerical_cols)
df_num = df[numerical_cols]

#Görev 2.3  ### Merkezi eğilim ve dağılım istatistikleri ###
summary_stats = pd.DataFrame()

summary_stats["Ortalama"] = df_num.mean()
summary_stats["Medyan"] = df_num.median()
summary_stats["Standart Sapma"] = df_num.std()
summary_stats["Minimum"] = df_num.min()
summary_stats["1. Çeyrek (Q1)"] = df_num.quantile(0.25)
summary_stats["3. Çeyrek (Q3)"] = df_num.quantile(0.75)
summary_stats["Maksimum"] = df_num.max()
summary_stats["IQR"] = summary_stats["3. Çeyrek (Q3)"] - summary_stats["1. Çeyrek (Q1)"]

summary_stats = summary_stats.round(2)
summary_stats
# summary_stats: Veri setinde yer alan sayısal değişkenlere ilişkin temel istatistiksel özet aşağıda sunulmuştur.
# Bu özet, merkezi eğilim (ortalama, medyan), dağılım ölçüleri (standart sapma, minimum, maksimum) ve çeyrekler arası açıklık (IQR) gibi temel istatistikleri içermektedir.

#                                    Ortalama   Medyan  Standart Sapma  Minimum  1. Çeyrek (Q1)  3. Çeyrek (Q3)  Maksimum      IQR
# Unnamed: 0                         51951.50  51951.5        29994.65      0.0        25975.75        77927.25  103903.0  51951.5
# id                                 64924.21  64856.5        37463.81      1.0        32533.75        97368.25  129880.0  64834.5
# Age                                   39.38     40.0           15.11      7.0           27.00           51.00      85.0     24.0
# Flight Distance                     1189.45    843.0          997.15     31.0          414.00         1743.00    4983.0   1329.0
# Inflight wifi service                  2.73      3.0            1.33      0.0            2.00            4.00       5.0      2.0
# Departure/Arrival time convenient      3.06      3.0            1.53      0.0            2.00            4.00       5.0      2.0
# Ease of Online booking                 2.76      3.0            1.40      0.0            2.00            4.00       5.0      2.0
# Gate location                          2.98      3.0            1.28      0.0            2.00            4.00       5.0      2.0
# Food and drink                         3.20      3.0            1.33      0.0            2.00            4.00       5.0      2.0
# Online boarding                        3.25      3.0            1.35      0.0            2.00            4.00       5.0      2.0
# Seat comfort                           3.44      4.0            1.32      0.0            2.00            5.00       5.0      3.0
# Inflight entertainment                 3.36      4.0            1.33      0.0            2.00            4.00       5.0      2.0
# On-board service                       3.38      4.0            1.29      0.0            2.00            4.00       5.0      2.0
# Leg room service                       3.35      4.0            1.32      0.0            2.00            4.00       5.0      2.0
# Baggage handling                       3.63      4.0            1.18      1.0            3.00            5.00       5.0      2.0
# Checkin service                        3.30      3.0            1.27      0.0            3.00            4.00       5.0      1.0
# Inflight service                       3.64      4.0            1.18      0.0            3.00            5.00       5.0      2.0
# Cleanliness                            3.29      3.0            1.31      0.0            2.00            4.00       5.0      2.0
# Departure Delay in Minutes            14.82      0.0           38.23      0.0            0.00           12.00    1592.0     12.0
# Arrival Delay in Minutes              15.18      0.0           38.70      0.0            0.00           13.00    1584.0     13.0

#### Temel Gözlemler:
## Yolcu yaşları ortalama olarak 39.4 civarındadır ve dağılımı 7 ile 85 arasında değişmektedir. Yaş değişkeni simetrik bir dağılıma sahiptir (medyan ≈ ortalama).

## Uçuş mesafesi (Flight Distance) geniş bir dağılıma sahiptir. Ortalama 1189 mil iken, minimum 31 ve maksimum 4983 olarak gözlemlenmiştir.
#Standart sapmanın (997) yüksek olması, verinin oldukça yaygın olduğunu gösterir.

## Servis kalitesiyle ilgili değerlendirme değişkenleri genellikle 0–5 arasında puanlanan kategorik sayısal değerlerdir.
#(örneğin: Inflight wifi service, Food and drink, Seat comfort vb.). Bu değişkenlerin çoğunun ortalamaları 2.7 ile 3.6 arasında değişmektedir, bu da kullanıcı deneyimlerinin ortalama seviyede olduğunu düşündürmektedir.

## Uçuş gecikmeleri ile ilgili değişkenlerde (Departure Delay ve Arrival Delay), medyan değerler 0'dır.
#Bu da çoğu uçuşun zamanında gerçekleştiğini, ancak bazı uçuşların oldukça yüksek gecikmelere (maksimum 1584–1592 dakikaya kadar) maruz kaldığını göstermektedir.
#Bu dağılım çarpıktır ve bazı uç nokta değerler aykırı olarak değerlendirilebilir.

## Seat comfort, Leg room service, Inflight entertainment gibi konforla ilgili değişkenlerin medyanları 4’tür, bu da birçok kullanıcının bu hizmetleri iyi değerlendirdiğini göstermektedir.

## Checkin service değişkeninin IQR değeri oldukça düşüktür (1.0), bu da kullanıcıların bu hizmette daha tutarlı geri bildirimler verdiğini düşündürür.

## Arrival Delay in Minutes ve Departure Delay in Minutes değişkenleri için ortalamalar sırasıyla 15.2 ve 14.8 dakikadır, ancak medyanın 0 olması, gecikmelerin büyük kısmının birkaç ekstrem durumda yoğunlaştığını gösterir.


# GÖREV 3  ### Eksik Değer Analizi ###
# Veri setindeki eksik değerlerin tespiti ve bu değerlerle ilgili uygulanabilecek yaklaşımlar açıklanır.

#Görev 3.1  ### Eksik değer sayısı ve oranı ###
missing_count = df.isnull().sum()
missing_percent = 100 * df.isnull().sum() / len(df)

missing_df = pd.DataFrame({
    'Eksik Değer Sayısı': missing_count,
    'Eksik Değer Oranı (%)': missing_percent.round(2)})

missing_df = missing_df[missing_df['Eksik Değer Sayısı'] > 0]
missing_df.sort_values(by='Eksik Değer Oranı (%)', ascending=False, inplace=True)
missing_df
#                                   Eksik Değer Sayısı  Eksik Değer Oranı (%)
# Arrival Delay in Minutes                 310                    0.3

#Görev 3.2  ### Eksik değeri olan satırları sil ###
df_cleaned = df.dropna()
print("Yeni veri seti boyutu:", df_cleaned.shape)           # Yeni veri seti boyutu: (103594, 25)


# GÖREV 4  ### Aykırı Değer (Outlier) Analizi ###
# Sayısal değişkenler üzerinde aykırı değerler belirlenir ve görsel/istatistiksel yöntemlerle raporlanır.

#Görev 4.1  ### Tüm sayısal değişkenler için aykırı değerlerin tespiti ###
def detect_outliers_iqr(dataframe, column):
    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = dataframe[(dataframe[column] < lower_bound) | (dataframe[column] > upper_bound)]
    return outliers


#Görev 4.2  ### Sayısal değişkenler üzerinden dön
numerical_cols = df_cleaned.select_dtypes(include=["int64", "float64"]).columns
outlier_summary = {}

for col in numerical_cols:
    outliers = detect_outliers_iqr(df_cleaned, col)
    count = outliers.shape[0]
    outlier_summary[col] = count

#Görev 4.3  ### Sonuçları tablolaştırılması ###
outlier_df = pd.DataFrame.from_dict(outlier_summary, orient='index', columns=["Aykırı Değer Sayısı"])
outlier_df = outlier_df.sort_values(by="Aykırı Değer Sayısı", ascending=False)
outlier_df

### Aykırı Değer (Outlier) Analizi – Rapor

# Veri setindeki sayısal değişkenler üzerinde IQR (Interquartile Range) yöntemiyle yapılan aykırı değer analizi sonucunda, aşağıdaki bulgulara ulaşılmıştır:
## Departure Delay in Minutes değişkeninde 14.428 aykırı değer tespit edilmiştir.

## Arrival Delay in Minutes değişkeninde 13.954 aykırı değer yer almaktadır.

## Bu değişkenlerdeki yüksek sayıda aykırı değer, havacılık sektöründeki uçuş gecikmelerinin genellikle normalin dışında seyretme eğiliminde olduğunu göstermektedir.
#Uçuşların büyük çoğunluğu zamanında yapılmakta, ancak az sayıda uçuşta çok yüksek gecikmeler yaşanmakta ve bu da çarpık bir dağılıma yol açmaktadır.

## Checkin service değişkeninde 12.853 aykırı değer bulunmuştur. Bu değer, hizmet memnuniyetine dayalı puanlamanın bazı yolcular tarafından aşırı yüksek ya da düşük verilmesinden kaynaklanıyor olabilir.
#Fakat 0-5 aralığındaki bir ölçek için bu kadar aykırı değer beklenmez; bu durumda aykırı değer algısı, verinin dağılımının dar olmasından kaynaklanıyor olabilir.

## Flight Distance değişkeninde 2.287 aykırı değer yer almaktadır. Bu da uçuş mesafelerinin genellikle belli bir aralıkta kümelendiğini, ancak bazı uçuşların çok kısa ya da çok uzun olduğunu göstermektedir.

### Bu proje analiz odaklı olduğu için, aykırı değerler şimdilik dokunulmadan bırakılmıştır. Modelleme yapılmayacağı için bu değerlerin etkisi şu aşamada problem teşkil etmemektedir.


# GÖREV 5  ### Görselleştirme ###
# Sayısal ve kategorik değişkenler için uygun grafik türleri kullanılarak veriler görselleştirilir.

# 1. Sayısal Değişkenler için Görselleştirme
# Histogram (Dağılımı görmek için)
df_cleaned.select_dtypes(include=["int64", "float64"]).hist(bins=30, figsize=(16, 12), color='skyblue', edgecolor='black')
plt.suptitle("Sayısal Değişkenlerin Histogramları", fontsize=16)
plt.tight_layout()
plt.show()

# Boxplot (Aykırı değerleri görmek için)
for col in df_cleaned.select_dtypes(include=["int64", "float64"]).columns:
    plt.figure(figsize=(8, 2))
    sns.boxplot(data=df_cleaned, x=col, color='lightcoral')
    plt.title(f"{col} - Boxplot")
    plt.show()


# 2. Kategorik Değişkenler için Görselleştirme
# Barplot / Countplot
categorical_cols = df_cleaned.select_dtypes(include='object').columns

for col in categorical_cols:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df_cleaned, x=col, order=df_cleaned[col].value_counts().index, palette='pastel')
    plt.title(f"{col} - Kategori Dağılımı")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

df.head()

# EKSTRA  ### Heatmap ile Kategorik Değişkenler Arası İlişki
sns.heatmap(pd.crosstab(df_cleaned["Class"], df_cleaned["Customer Type"]), annot=True, cmap="YlGnBu")





# EKSTRA  ### Bağımlı Değişken Analizi ###

