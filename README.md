# PYTHON- E-TİCARET

Python dili kullanarak geliştirilmiş bir e-ticaret API projesi.

## 1) Ürün yönetimi için başlangıç mimarisi

Bu aşamada **FastAPI + SQLAlchemy + Pydantic** üçlüsüyle başlamak en doğru ve temiz yaklaşım olur:

- **FastAPI**: Hızlı, tip güvenli ve dokümantasyonu otomatik üretir.
- **SQLAlchemy**: Veritabanı katmanını modüler ve yönetilebilir tutar.
- **Pydantic**: İstek/yanıt doğrulamasını güvenli ve net hale getirir.

## 2) Klasör yapısı

```text
python_eticaret/
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── models/
│   │   └── product.py
│   ├── schemas/
│   │   └── product.py
│   ├── crud/
│   │   └── product.py
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   └── products.py
│   │       └── router.py
│   └── main.py
├── requirements.txt
└── README.md
```

Bu yapı ile sorumluluklar ayrılır:
- `models`: Veritabanı tabloları
- `schemas`: API giriş/çıkış modelleri
- `crud`: Veritabanı işlemleri
- `api`: Endpoint ve route yönetimi
- `core`: Ayarlar ve DB bağlantısı

## 3) Kurulacak kütüphaneler

`requirements.txt` dosyasındaki temel paketler:

- `fastapi`
- `uvicorn[standard]`
- `sqlalchemy`
- `pydantic`
- `alembic`
- `python-dotenv`

## 4) Kurulum adımları

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 5) Sonraki adım

Sonraki adımda `Product` modeli için:
- `id`, `name`, `description`, `price`, `stock`, `is_active`, `created_at`
alanlarıyla modeli oluşturup,
- ürün listeleme/ekleme/getirme/güncelleme/silme endpoint’lerini yazacağız.


