# PYTHON- E-TİCARET API

Django ve Django REST Framework merkezli, modüler yapıya sahip e-ticaret API'si. Proje, asenkron ve yüksek performanslı işlemler için FastAPI altyapısını da barındırmaktadır.

## Özellikler

* Modüler mimari: Ürünler, siparişler, kategoriler, kullanıcılar ve yorumlar için izole edilmiş uygulamalar.
* DRF Serializer seviyesinde gelişmiş veri doğrulama (negatif stok engelleme, fiyat sınırlandırması, regex ile slug format kontrolü).
* Temel ürün yönetimi için RESTful uç noktalar (GET, POST, PUT).

## Temel Teknolojiler

* Django 6.0.6 & Django REST Framework
* FastAPI, Uvicorn, Pydantic
* SQLite3, SQLAlchemy, Alembic

## Kurulum ve Çalıştırma

Geliştirme ortamını hazırlamak için terminalinizde sırasıyla şu komutları çalıştırabilirsiniz:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

Sunucuları başlatmak için ise şu komutları kullanabilirsiniz:

**Django Servisi:**
```bash
python manage.py runserver
```

**FastAPI Servisi:**
```bash
uvicorn main:app --reload
```
