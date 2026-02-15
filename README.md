# AI Adaptive Learning System (ICT UAS)

Sistem Pembelajaran Adaptif Berbasis Artificial Intelligence (AI) berbasis web yang mampu:

- Menganalisis performa belajar pengguna
- Menentukan tingkat pembelajaran (Pemula / Menengah / Lanjutan)
- Mengelompokkan gaya belajar
- Memberikan rekomendasi materi adaptif
- Menghitung skor dan waktu pengerjaan secara otomatis

Project ini dikembangkan sebagai tugas UAS mata kuliah ICT Literacy.

---

## 🚀 Fitur Utama

- 5 Mata Kuliah / Jenis Soal
- 10 Soal Pilihan Ganda per Mata Kuliah
- Perhitungan skor otomatis
- Perhitungan waktu pengerjaan otomatis (server-side session)
- Model Machine Learning (Decision Tree - scikit-learn)
- Analisis gaya belajar (rule-based)
- Rekomendasi materi adaptif
- Tampilan web responsif

---

## 🧠 Teknologi yang Digunakan

| Teknologi | Versi |
|-----------|-------|
| Python | 3.10.x |
| Flask | 2.x |
| scikit-learn | 1.x |
| pandas | 2.x |
| joblib | 1.x |
| HTML & CSS | - |
| Conda (environment) | Terbaru |

⚠️ Direkomendasikan menggunakan Python 3.10 (bukan 3.13/3.15 alpha).

---

## 📂 Struktur Project

```
ict-ai-learning/
│
├── app.py
├── train_model.py
├── model.pkl
├── data.csv
├── questions.py
│
├── templates/
│   ├── index.html
│   ├── quiz.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── quiz.css
│
└── README.md
```

---

## 📸 Screenshot Aplikasi
* Halaman Input
![/screenshots/input.png](screenshots/input.png)

* Halaman Hasil Analisis
![/screenshots/output.png](screenshots/output.png)

---

## 🛠️ Cara Setup Project

### 1️⃣ Clone Repository

```bash
git clone <repository-url>
cd ict-ai-learning
```

---

### 2️⃣ Buat Environment (Disarankan: Conda)

```bash
conda create -n ict-ai python=3.10 scikit-learn pandas flask joblib -y
conda activate ict-ai
```

Pastikan environment aktif:

```bash
(ict-ai)
```

---

### 3️⃣ Training Model AI

Jika file `model.pkl` belum ada:

```bash
python train_model.py
```

Ini akan menghasilkan file:

```
model.pkl
```

---

### 4️⃣ Jalankan Aplikasi

```bash
python app.py
```

Jika berhasil, akan muncul:

```
Running on http://127.0.0.1:5000
```

---

### 5️⃣ Buka di Browser

```
http://127.0.0.1:5000
```

---

## 📊 Cara Kerja Sistem

1. User memilih mata kuliah
2. User mengerjakan 10 soal pilihan ganda
3. Sistem menghitung:
   - Skor
   - Waktu pengerjaan
4. Model AI menganalisis performa
5. Sistem menampilkan:
   - Tingkat pembelajaran
   - Gaya belajar
   - Rekomendasi materi

---

## 🧪 Model AI

Model menggunakan:

- Decision Tree Classifier
- Input:
  - Skor kuis
  - Waktu pengerjaan
- Output:
  - Pemula
  - Menengah
  - Lanjutan

---

## 🛑 Troubleshooting

### Error: start_time not defined
Pastikan `start_time` hanya disimpan di session, bukan dikirim ke template.

### Error: scikit-learn gagal install
Gunakan Python 3.10 (hindari Python 3.15 alpha).

### Error: model.pkl tidak ditemukan
Jalankan:
```bash
python train_model.py
```

---

## 👨‍💻 Developer

Andhika Bagaskara Putra Nusantara  
PJJ Informatika  
Universitas Islam Indragiri  
ICT Literacy – UAS Project

---

## 📌 Catatan

Project ini merupakan prototipe akademik untuk keperluan pembelajaran dan penelitian, bukan sistem produksi.