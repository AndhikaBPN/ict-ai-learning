# AI Adaptive Learning System

Prototipe sistem pembelajaran adaptif berbasis Artificial Intelligence (AI) untuk menganalisis performa belajar siswa dan mengklasifikasikan tingkat pembelajaran secara otomatis.

Project ini dikembangkan untuk mata kuliah **ICT Literacy**.

---

## ✨ Fitur Utama
- Analisis performa siswa berdasarkan:
  - Nilai kuis
  - Waktu pengerjaan
- Klasifikasi tingkat pembelajaran:
  - Pemula
  - Menengah
  - Lanjutan
- Aplikasi berbasis web
- Tampilan sederhana dengan indikator warna tiap level
- Menggunakan machine learning (Decision Tree)

---

## 🧠 Teknologi
- Python 3.10
- Flask
- scikit-learn
- pandas
- HTML & CSS
- Conda

---

## 📂 Struktur Project
ict-ai-learning/
├── app.py
├── train_model.py
├── model.pkl
├── data.csv
│
├── templates/
│ ├── index.html
│ └── result.html
│
└── static/
└── style.css

---

## 🚀 Setup & Menjalankan Project

### 1. Clone Repository
```bash
git clone <repo-url>
cd ict-ai-learning
```


## Buat environment
```bash
conda create -n ict-ai python=3.10 scikit-learn pandas flask joblib -y
conda activate ict-ai
```

## Training Model AI
```bash
python train_model.py
```

## Jalankan Aplikasi
```bash
python app.py
```

## 🧪 Contoh Input & Output
Contoh 1
Input
* Nilai Kuis: 90
* Waktu Pengerjaan: 8 menit

Output
* Tingkat Pembelajaran: Lanjutan (🟢)

Contoh 2
Input
* Nilai Kuis: 65
* Waktu Pengerjaan: 18 menit

Output
* Tingkat Pembelajaran: Menengah (🟡)

Contoh 3

Input
* Nilai Kuis: 40
* Waktu Pengerjaan: 30 menit

Output
* Tingkat Pembelajaran: Pemula (🔴)

## 📸 Screenshot Aplikasi
* Halaman Input
![alt text](screenshots/input.png)

* Halaman Hasil Analisis
![/screenshots/result.png](screenshots/output.png)