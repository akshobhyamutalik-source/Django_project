# 🐾 TeddyPups U.A.E. — Premium Teacup Puppies in Dubai
### A Complete Full-Stack Clone of [https://puppy.instabizweb.com/](https://puppy.instabizweb.com/)
**Built for Blutec AI Technical Round Assessment by Akshobhya**

---

## 🌟 Project Overview

This repository contains a full-stack, responsive web application cloning the design, layout, responsiveness, and functionality of **TeddyPups U.A.E.** (reference site: [https://puppy.instabizweb.com/](https://puppy.instabizweb.com/)).

It is developed with clean, beginner-friendly **Python Django**, **Bootstrap 5**, and **SQLite3**, adhering strictly to modern web development standards and decoupled MVT architecture.

---

## 🚀 Pages & Features Cloned (1:1 Match)

| Route | Page | Features |
|---|---|---|
| `/` | **Home** | Luxury Hero, "Meet the pups", "Two ways to meet your puppy", "Your puppy journey", "Why families trust us", and Call-to-Action. |
| `/puppies/` | **Available Puppies** | Filterable catalog by breed + **"Already gone home"** adopted showcase. |
| `/puppies/<id>/` | **Puppy Details** | High-res photo, price in AED, health kit checklist, "Enquire on WhatsApp", and "Other puppies you might love" recommendations. |
| `/happy-families/` | **Happy Families** | Client testimonials and photo gallery of delivered puppies with pet parents across Dubai & U.A.E. |
| `/how-it-works/` | **How It Works** | "Two ways home" (Downtown Dubai showroom vs. Bespoke Korea/Europe import), "Premium puppy promise", and delivery details. |
| `/faq/` | **Questions & Answers** | Exact 7 accordion Q&As answering vaccination, flight transport, and viewing guidelines. |
| `/contact/` | **Visit & Contact** | Downtown Dubai showroom location, visiting hours, contact form with automated puppy pre-selection, and WhatsApp link. |
| `/admin/` | **Admin Portal** | Custom branded dashboard with photo thumbnail previews, search bars, and inline table editing. |

---

## 🛠️ Technology Stack

* **Backend:** Python 3 & Django Framework (Function-Based Views, ORM, ModelForms, CSRF Protection)
* **Database:** SQLite3 (`db.sqlite3`)
* **Frontend:** HTML5 with Django Template Inheritance (`base.html`), Bootstrap 5, Bootstrap Icons
* **Styling:** Custom CSS with luxury cream (`#FDFBF7`) & camel gold (`#C5A880`) palette
* **Communication:** Direct WhatsApp Click-to-Chat protocol (`https://wa.me/919898124987`)
* **Testing:** 15 automated unit tests (`django.test.TestCase`)

---

## ⚙️ How to Setup & Run Locally

```bash
# 1. Clone repository
git clone https://github.com/<your-username>/puppy-website-clone.git
cd puppy-website-clone

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply database migrations
python manage.py migrate

# 4. Run automated test suite (All 15 tests pass)
python manage.py test

# 5. Start development server
python manage.py runserver
```

Open your browser at: `http://127.0.0.1:8000/`

---

## 🔐 Admin Login Credentials

* **URL:** `http://127.0.0.1:8000/admin/`
* **Username:** `admin`
* **Password:** `admin123`

---

## 🧪 Automated Unit Test Report

Run `python manage.py test` to execute all 15 test cases:
* **`home/tests.py` (4 tests):** Tests HTTP 200 and templates for Home, Happy Families, How It Works, and FAQ.
* **`puppies/tests.py` (6 tests):** Tests Puppy model string representation, WhatsApp link generation, list view, valid puppy details (200 OK), non-existent puppy (404), and breed search filtering.
* **`enquiries/tests.py` (5 tests):** Tests Enquiry model, Form validation with valid data, rejection on missing fields, GET contact view, and POST submission saving record into SQLite with success feedback alert.

---

## 🎥 Loom Video Recording Outline

1. **Introduction (0:00 - 0:45):** Introduce yourself (Akshobhya) and the goal: cloning https://puppy.instabizweb.com/.
2. **Feature Demo (0:45 - 2:00):** Walk through Home, Available Puppies (Max the Maltipoo), breed search, Happy Families, How It Works, and submit an enquiry form.
3. **Architecture & Code (2:00 - 3:15):** Show Django MVT structure (`models.py`, `views.py`, `forms.py`, `base.html`).
4. **AI Tools Policy (3:15 - 4:00):** Explain the prompts used with Antigravity AI to plan, scaffold, and refine the clone.
5. **Testing & Deployment (4:00 - 5:00):** Run `python manage.py test` in terminal showing 15/15 tests passing, and show the live deployed site.
