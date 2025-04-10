🎮 Event Manager API
سیستم مدیریت ایونت‌ها (رویدادها) با قابلیت عضویت، ترک ایونت، لاگ‌گیری دقیق و کنترل کامل توسط سازنده رویداد.

🧩 ویژگی‌ها
ساخت ایونت با ظرفیت مشخص، توضیحات و وضعیت باز/بسته.

عضویت در ایونت‌ها (فقط وقتی ایونت باز باشه و ظرفیت نداشته باشه).

ترک ایونت توسط اعضا در هر لحظه.

لیست اعضای هر ایونت با شناسه (ID) و نام کاربری.

مدیریت کامل ایونت‌ها توسط سازنده (ویرایش، حذف).

ثبت لاگ برای هر اکشن (عضویت، ترک، ساخت، حذف و ...).

نمایش لاگ فقط برای سازنده ایونت‌ها.

📁 ساختار دیتابیس
- name
- description
- capacity
- status: [open | closed]
- creator: ForeignKey(User)


EventMembership:

- user: ForeignKey(User)
- event: ForeignKey(Event)
- joined_at


EventLog:

- event: ForeignKey(Event)
- action: string (مثلاً "Ali joined the event")
- metadata: string (مثلاً "joined via API")
- timestamp: auto_now_add



🚀 API Endpoint ها
✅ Event
GET /events/ → لیست تمام ایونت‌ها

POST /events/ → ساخت ایونت

GET /events/{id}/ → اطلاعات یک ایونت خاص

PUT /events/{id}/ → ویرایش ایونت (فقط سازنده)

DELETE /events/{id}/ → حذف ایونت (فقط سازنده)

✅ Membership
POST /events/{id}/join/ → عضویت در ایونت

DELETE /events/{id}/exit/ → ترک ایونت

✅ Members
GET /events/{id}/members/ → اعضای ایونت (فقط توسط سازنده)

✅ Logs
GET /logs/ → نمایش لاگ‌های ایونت‌هایی که خود کاربر سازنده‌شونه

GET /logs/{event_id}/ → فقط اگه کاربر سازنده اون ایونت باشه


🛠 تکنولوژی‌ها
Django & Django REST Framework

SQLite (قابل ارتقا به PostgreSQL)

JWT Authentication / Session-based (بسته به تنظیمات)


