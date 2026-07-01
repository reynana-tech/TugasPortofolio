# 🚀 QUICK START - DEPLOY KE VERCEL

## 1️⃣ PERSIAPAN (5 menit)

### Step 1: Push ke GitHub
```bash
git add .
git commit -m "Ready for Vercel deployment"
git push origin main
```

### Step 2: Generate SECRET_KEY
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
# Copy hasilnya (contoh: a1b2c3d4e5f6...)
```

## 2️⃣ SETUP DI VERCEL (10 menit)

### Step 1: Login ke Vercel
1. Buka https://vercel.com/dashboard
2. Klik "New Project"
3. Pilih repository Anda dari GitHub
4. Klik "Import"

### Step 2: Setup Environment Variables
Di halaman "Environment Variables", tambahkan:

```
TIDB_HOST=<ask your database provider>
TIDB_PORT=4000
TIDB_USER=<your username>
TIDB_PASSWORD=<your password>
TIDB_DB=db_porto
TIDB_SSL_CA=/etc/ssl/certs/ca-certificates.crt
SECRET_KEY=<paste hasil dari Step 2 di atas>
FLASK_ENV=production
ADMIN_USERNAME=admin
ADMIN_PASSWORD=<secure password>
```

### Step 3: Deploy!
1. Klik "Deploy"
2. Tunggu sampai selesai (biasanya 2-3 menit)
3. Ambil URL aplikasi Anda

## 3️⃣ VERIFIKASI (5 menit)

### Test aplikasi dengan membuka:
- `https://your-app.vercel.app/` → Homepage
- `https://your-app.vercel.app/health` → Health check
- `https://your-app.vercel.app/admin/login` → Login page

### Jika ada error:
1. Buka Vercel Dashboard
2. Klik "Deployments"
3. Klik "Function logs" untuk melihat error details
4. Fix dan push ulang ke GitHub

## 🔍 COMMON ISSUES

### ❌ "Internal Server Error"
**Solusi:**
1. Check TIDB credentials di Vercel settings
2. Pastikan TiDB bisa diakses dari Vercel
3. Lihat logs di Vercel Dashboard

### ❌ "Module not found: model"
**Solusi:** Pastikan file `model.py` ada di root directory

### ❌ "Database connection error"
**Solusi:**
1. Verify TIDB_HOST, TIDB_USER, TIDB_PASSWORD
2. Add your Vercel IP ke TiDB firewall rules

## ✅ SEHARUSNYA BERFUNGSI

Semua ini sudah diperbaiki:
- ✅ WSGI entry point (`index.py`)
- ✅ Vercel config (`vercel.json`)
- ✅ Static files handling
- ✅ Database error handling
- ✅ Environment variables support
- ✅ Graceful degradation

## 📚 Dokumentasi Lengkap

- **DEPLOYMENT_VERCEL.md** - Panduan detail lengkap
- **VERCEL_CHANGES_SUMMARY.md** - Daftar semua perubahan

---

**Sukses!** 🎉 Aplikasi Anda siap di-deploy ke Vercel!
