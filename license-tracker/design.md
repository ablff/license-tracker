# License Tracker — Database Design

## Table: users

* `id`: Integer, primary key
* `name`: String(100), required
* `email`: String(100), unique


## Table: licenses

* `id`: Integer, primary key
* `title`: String(150), required
* `license_number`: String(100), optional
* `license_type`: previous_license_id, Integer, foreign key -> licenses.id String(100), required
* `issuing_authority`: String(150), optional
* `expiration_date`: Date, optional
* `reminder_date`: Date, optional
* `status`: "pending, in_progress, under_review, approved, rejected, renewed, cancelled" String(50), required
* `description`: Text, optional
* `created_at`: DateTime, required
* `owner_id`: Integer, foreign key -> users.id, required

## Relationship

* One user can have many licenses or tracked licensing processes.
* Each license or tracked process belongs to one user.
* The foreign key `owner_id` is stored in `licenses` and references `users.id`.

## Questions the API Should Answer

1. Which licenses or tracked processes will expire in the next 30 days?
2. Which licenses or tracked processes require action today or have overdue deadlines?
3. What licenses, documents, or licensing processes are associated with a specific user, and what is the current status of each?
