
# ✈️ Airline Passenger Satisfaction - EDA Raporu

Bu çalışma, Airline Passenger Satisfaction veri seti üzerinde Keşifsel Veri Analizi (EDA) yapılmasını kapsamaktadır. Projede yalnızca analiz yapılmış, herhangi bir modelleme yapılmamıştır.

---

## 📌 GÖREV 1: Veri Seti Seçimi

- Kaggle üzerinden alınan `train.csv` dosyası analizde kullanılmıştır.
- Veri seti boyutu: 103904 satır, 25 sütun.

---

## 📊 GÖREV 2: İstatistiksel Özet

- Sayısal değişkenler için ortalama, medyan, standart sapma, minimum, maksimum, çeyrek değerler ve IQR hesaplanmıştır.

### Öne Çıkan Bulgular:

- **Yaş ortalaması**: 39.4 (dağılım 7–85 arası)
- **Uçuş mesafesi**: Ortalama 1189 mil, maksimum 4983
- **Servis puanları**: Genelde 0–5 aralığında, ortalamalar 2.7–3.6 arasında
- **Gecikme süreleri**: Medyan = 0, ancak maksimumlar 1500 dakikayı geçebiliyor

---

## 🔍 GÖREV 3: Eksik Değer Analizi

- Sadece `Arrival Delay in Minutes` değişkeninde eksik veri mevcuttu (310 adet, %0.3).
- Eksik değer içeren satırlar veri setinden **silinmiştir**.
- Yeni veri seti boyutu: 103594 satır

---

## 🚨 GÖREV 4: Aykırı Değer Analizi

- IQR yöntemine göre aykırı değerler belirlendi.
- Özellikle gecikme ve bazı servis değişkenlerinde yüksek sayıda aykırı değer gözlendi:

| Değişken                    | Aykırı Değer Sayısı |
|-----------------------------|---------------------|
| Departure Delay             | 14,428              |
| Arrival Delay               | 13,954              |
| Checkin service             | 12,853              |
| Flight Distance             | 2,287               |

> Analiz amaçlı çalışmalarda aykırı değerlere müdahale edilmemiştir.

---

## 📈 GÖREV 5: Görselleştirme

### Sayısal Değişkenler
- Histogram ve boxplot grafiklerle dağılım ve aykırılıklar incelenmiştir.

### Kategorik Değişkenler
- Countplot ile tüm kategorik değişkenlerin dağılımı görselleştirilmiştir.

---

## 📁 Dosya Yapısı (Önerilen)

```
📦 airline_satisfaction_project/
├── data/
│   └── train.csv
├── eda_airline_satisfaction.py
└── RAPOR.md
```

---

## 👤 Hazırlayan

**İsim:** İrem Kocagöz  
**Tarih:** Haziran 2025  
**Veri Kaynağı:** [Kaggle – Teejmahal20](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)
