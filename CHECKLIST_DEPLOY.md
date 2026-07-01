# ✅ FINAL CHECKLIST - DEPLOY KE VERCEL

Baca dokumen ini sebelum deploy!

## 📍 VERIFIKASI LOKAL (5 min)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run aplikasi
python app.py

# 3. Buka http://localhost:5000
# 4. Pastikan berfungsi tanpa error
```

**✅ Jika semua OK, lanjut ke langkah berikutnya**

---

## 🔑 SIAPKAN CREDENTIALS

### Generate SECRET_KEY
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```
Simpan hasilnya! (Contoh: `a1b2c3d4e5f6...`)

### Siapkan TIDB Info
- TIDB_HOST = ?
- TIDB_USER = ?
- TIDB_PASSWORD = ?
- TIDB_DB = db_porto (biasanya)

---

## 🚀 DEPLOY LANGKAH DI VERCEL

### Step 1: Push ke GitHub
```bash
git add .
git commit -m "Ready for Vercel"
git push origin main
```

### Step 2: Buka Vercel Dashboard
1. Pergi ke https://vercel.com/dashboard
2. Klik "New Project"
3. Pilih repository Anda
4. Klik "Import"

### Step 3: Set Environment Variables
Klik "Environment Variables" dan tambahkan:

```
TIDB_HOST = [YOUR_HOST]
TIDB_PORT = 4000
TIDB_USER = [YOUR_USER]
TIDB_PASSWORD = [YOUR_PASSWORD]
TIDB_DB = db_porto
TIDB_SSL_CA = /etc/ssl/certs/ca-certificates.crt
SECRET_KEY = [HASIL GENERATE DI ATAS]
FLASK_ENV = production
ADMIN_USERNAME = admin
ADMIN_PASSWORD = [YOUR_PASSWORD]
```

### Step 4: Deploy!
1. Klik "Deploy"
2. Tunggu ± 3 menit
3. Ambil URL aplikasi

---

## ✔️ TESTING SETELAH DEPLOY

Buka di browser:

1. **Homepage**
   ```
   https://your-app.vercel.app/
   ```
   ✅ Harus tampil halaman portofolio

2. **Health Check**
   ```
   https://your-app.vercel.app/health
   ```
   ✅ Harus return: `{"status": "ok"}`

3. **Admin Login**
   ```
   https://your-app.vercel.app/admin/login
   ```
   ✅ Harus tampil halaman login

4. **API Test**
   ```
   https://your-app.vercel.app/api/profile
   ```
   ✅ Harus return data dalam JSON

---

## ❌ JIKA ADA ERROR

### Error: "Internal Server Error (500)"
1. Buka Vercel Dashboard
2. Klik "Deployments"
3. Klik "Function logs"
4. Cari error message
5. Fix & push ulang

**Penyebab umum:**
- ❌ TIDB credentials salah
- ❌ TIDB host tidak bisa diakses dari Vercel
- ❌ Environment variables belum lengkap
- ❌ SECRET_KEY belum diset

### Error: "Module not found"
- Pastikan file `model.py` ada di folder root
- Pastikan `requirements.txt` complete

### Error: "Static files 404"
- Sudah diperbaiki di `app.py`
- Jika masih ada issue, check `Frontend` folder structure

---

## 📊 STRUKTUR FOLDER HARUS BEGINI

```
.
├── app.py ✅
├── model.py ✅
├── config.py ✅
├── index.py ✅ (BARU)
├── vercel.json ✅ (BARU)
├── requirements.txt ✅
├── Frontend/ ✅
│   ├── admin/
│   ├── utama/
│   ├── css/
│   ├── js/
│   └── img/
├── Backend/ ✅
│   ├── admin/
│   └── utama/
└── README.md
```

Semua harus ada! Jika ada yang kurang, copy dari original.

---

## 🎯 QUICK LINKS

📖 **Dokumentasi Lengkap:**
- `QUICK_DEPLOY.md` - Versi singkat
- `DEPLOYMENT_VERCEL.md` - Lengkap + troubleshooting
- `VERCEL_CHANGES_SUMMARY.md` - Semua perubahan
- `README_DEPLOYMENT.md` - Ringkasan

---

## ✨ PERUBAHAN YANG SUDAH DILAKUKAN

✅ `app.py` - Fixed path handling & error handling
✅ `model.py` - Added error handling & connection management
✅ `config.py` - Added production validation
✅ `Backend/utama/utama.py` - Fixed all API endpoints
✅ `index.py` - Created WSGI entry point
✅ `vercel.json` - Created Vercel config
✅ `requirements.txt` - Added production packages

---

## 🎉 SELESAI!

**Aplikasi Anda siap di-deploy ke Vercel!**

Ikuti checklist di atas dengan teliti.

**Ada pertanyaan?** Baca file dokumentasi yang disediakan.

---

**Status: ✅ READY FOR PRODUCTION**
