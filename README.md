# 🎓 Event Management System

A **Web-based Event Management System** developed to simplify the management of college events, user registrations, and event participation.

The system provides separate **Admin** and **User** modules with event management, registration tracking, analytics, payment-flow simulation, and receipt generation.

---

## 📌 Project Overview

The **Event Management System** is a full-stack web application designed for colleges to manage technical and non-technical events efficiently.

It allows administrators to create and manage events, monitor registrations through a dashboard, and view analytics. Users can browse upcoming events, register for events, complete a sample UPI payment flow, download registration receipts, and view their registered events.

---

## ✨ Features

### 🔐 Admin Features

* Admin Login
* Admin Dashboard
* View total number of events
* View total registrations
* Technical vs Non-Technical registration analytics
* Event-wise registration analysis
* Add new events
* Edit existing events
* Delete events
* View registered users

### 👤 User Features

* User Registration
* User Login
* Browse upcoming events
* Search events
* Filter events
* Register for events
* Sample UPI payment flow
* Payment loading animation
* Registration confirmation
* Download registration receipt
* View registered events
* Logout

---

## 🛠️ Technologies Used

| Technology       | Purpose                                    |
| ---------------- | ------------------------------------------ |
| **HTML**         | Structure and page layout                  |
| **CSS**          | Styling and responsive UI                  |
| **JavaScript**   | Client-side functionality and interactions |
| **Flask**        | Backend web framework                      |
| **Python**       | Server-side programming                    |
| **MySQL**        | Database management                        |
| **SQLAlchemy**   | Database integration / ORM                 |
| **Font Awesome** | UI icons                                   |
| **Chart.js**     | Dashboard data visualization               |

---

## 🏗️ System Modules

### Admin Module

The Admin module provides complete control over the event management system.

**Admin → Login → Dashboard → Event Management → User Management → Analytics**

### User Module

The User module allows students to discover and register for events.

**User → Register/Login → Browse Events → Search/Filter → Register → Payment Flow → Receipt → Registered Events**

---

## 📊 Admin Dashboard

The dashboard provides a visual overview of the event system, including:

* Total Events
* Total Registrations
* Technical Event Registrations
* Non-Technical Event Registrations
* Event-wise Registration Statistics
* Registration Analytics

---

## 💳 Payment Flow

The project includes a **sample UPI payment flow** for demonstrating the event registration process.

### Flow:

```text
Select Event
     ↓
Register for Event
     ↓
Payment Page
     ↓
Enter UPI ID
     ↓
Payment Processing Animation
     ↓
Registration Confirmation
     ↓
Download Receipt
```

> **Note:** The payment module is a simulated payment flow created for project demonstration purposes and does not process real payments.

---

## 🧾 Registration Receipt

After successful event registration, users can download a registration receipt containing the relevant registration and event details.

---

## 🗄️ Database

The application uses **MySQL** to store and manage:

* User details
* Event details
* Registration details
* Payment information
* Event-related data

CRUD operations are implemented for efficient event management.

---

## 🔄 CRUD Operations

The Admin can perform:

* **Create** → Add new events
* **Read** → View events and users
* **Update** → Edit event details
* **Delete** → Remove events

---

## 🔒 Authentication

The application provides separate authentication flows for:

* Admin
* Users

Users can register, log in, access their event-related information, and securely log out of the system.

---

## 🚀 How It Works

1. Admin logs into the system.
2. Admin adds and manages college events.
3. Users create an account and log in.
4. Users browse upcoming events.
5. Users can search and filter available events.
6. Users select an event and complete registration.
7. The sample UPI payment flow is displayed.
8. A registration receipt can be downloaded.
9. Users can view their registered events.
10. Admin can monitor registrations through the dashboard.

---

## 🎯 Learning Outcomes

This project helped me strengthen my understanding of:

* Full-Stack Web Development
* Flask Web Application Development
* MySQL Database Integration
* SQLAlchemy ORM
* CRUD Operations
* User Authentication
* Session Management
* Form Handling
* Event Registration Systems
* Payment Flow Simulation
* Data Visualization
* PDF Receipt Generation
* Frontend and Backend Integration

---

## 🔮 Future Enhancements

Some possible future improvements include:

* Real payment gateway integration
* Email notifications
* Event reminder notifications
* QR-code based event check-in
* User profile management
* Admin role management
* Event attendance tracking
* Certificate generation
* Advanced registration analytics
* Responsive mobile-first design

---

## 💻 Project Status

**Completed ✅**

The project currently includes the core Admin and User functionalities required for managing college events and registrations.

---

SCREENSHOTS

<img width="1356" height="595" alt="Screenshot 2026-08-29 182004" src="https://github.com/user-attachments/assets/55aa5cdd-8496-4f2b-8ea1-72ceca601bf1" />
<img width="1349" height="599" alt="Screenshot 2026-08-29 182036" src="https://github.com/user-attachments/assets/755757ec-d7a3-4573-adab-f97780258a8b" />
<img width="1350" height="599" alt="Screenshot 2026-08-29 182057" src="https://github.com/user-attachments/assets/6b22d919-4061-40f0-9d47-a94b7b051f1f" />
<img width="1348" height="596" alt="Screenshot 2026-08-29 182108" src="https://github.com/user-attachments/assets/a70a0ea5-5783-402f-b0c0-82f9320d53fe" />
<img width="1348" height="590" alt="Screenshot 2026-08-29 182127" src="https://github.com/user-attachments/assets/722cd075-731c-45bd-95d7-f17930c78825" />
<img width="1346" height="599" alt="Screenshot 2026-08-29 183414" src="https://github.com/user-attachments/assets/e41566d8-a17c-47d6-9681-d9c3dfd04790" />
<img width="1352" height="595" alt="Screenshot 2026-08-29 183445" src="https://github.com/user-attachments/assets/f638e9f5-bead-418c-897a-f7f4f8a6c9c8" />
<img width="1357" height="588" alt="Screenshot 2026-08-29 183459" src="https://github.com/user-attachments/assets/e9f5cb87-724f-4d9b-a1fc-1afe7b7270c7" />
<img width="1289" height="409" alt="Screenshot 2026-08-29 183737" src="https://github.com/user-attachments/assets/4b8bf3c4-e061-432c-8ed5-7e763bebb01e" />
<img width="799" height="501" alt="Screenshot 2026-08-29 183748" src="https://github.com/user-attachments/assets/ba921b18-0e4c-4054-8975-af4c46a9072f" />
<img width="1365" height="597" alt="Screenshot 2026-08-29 183804" src="https://github.com/user-attachments/assets/378b2fd3-f0c1-43be-9bc1-6e408e1e7720" />
<img width="1340" height="589" alt="Screenshot 2026-08-29 183817" src="https://github.com/user-attachments/assets/e2577d9b-49f4-4c89-a08a-ab2f86ac0f71" />
<img width="1360" height="596" alt="Screenshot 2026-08-29 183828" src="https://github.com/user-attachments/assets/538afe9f-7853-42e9-9cb7-46615553547e" />
<img width="1352" height="592" alt="Screenshot 2026-08-29 183955" src="https://github.com/user-attachments/assets/54365ed2-7798-49b5-852f-f339a2f88b4f" />
<img width="1342" height="590" alt="Screenshot 2026-08-29 184006" src="https://github.com/user-attachments/assets/5e31d254-e862-41c9-97b1-9f34bf4b2c5a" />
<img width="1345" height="594" alt="Screenshot 2026-08-29 184100" src="https://github.com/user-attachments/assets/c3d15b44-ac46-4459-8ea3-3bdc78a159b1" />
<img width="1346" height="587" alt="Screenshot 2026-08-29 184412" src="https://github.com/user-attachments/assets/30e6c426-ac7e-4fea-8253-d66808c065fa" />
<img width="1351" height="599" alt="Screenshot 2026-08-29 184430" src="https://github.com/user-attachments/assets/d88bbf9d-cf9e-45d9-8a8a-817c5142f619" />
<img width="1357" height="601" alt="Screenshot 2026-08-29 184440" src="https://github.com/user-attachments/assets/30290f52-04a1-4f60-8553-f994a726bf60" />
<img width="1359" height="586" alt="Screenshot 2026-08-29 184540" src="https://github.com/user-attachments/assets/20e6cc68-078b-4812-8576-f0ba35a8ac9f" />
<img width="1348" height="594" alt="Screenshot 2026-08-29 184632" src="https://github.com/user-attachments/assets/33012e77-bb61-479e-ac49-847669c032e9" />
<img width="1365" height="588" alt="Screenshot 2026-08-29 184646" src="https://github.com/user-attachments/assets/ad26996f-6b25-467f-863c-56c4f5943b45" />
<img width="1351" height="602" alt="Screenshot 2026-08-29 184727" src="https://github.com/user-attachments/assets/f5bf249e-1e7d-4122-92da-a5243d471921" />
<img width="1310" height="447" alt="Screenshot 2026-08-29 184737" src="https://github.com/user-attachments/assets/548fe841-aa78-4d53-85ab-5b3e177bf2de" />
<img width="961" height="395" alt="Screenshot 2026-08-29 184819" src="https://github.com/user-attachments/assets/0b2353d3-e221-46c5-b6f4-0b8b4425b36e" />
<img width="1361" height="595" alt="Screenshot 2026-08-29 184854" src="https://github.com/user-attachments/assets/78aa43d7-eb64-4544-b229-63599460ded7" />
<img width="1340" height="582" alt="Screenshot 2026-08-29 184902" src="https://github.com/user-attachments/assets/1653bf89-ad87-4891-ae7d-4e610f206293" />
<img width="662" height="526" alt="Screenshot 2026-08-29 184923" src="https://github.com/user-attachments/assets/b1613569-3e2b-42c8-ad58-a666ea5f9b32" />
<img width="1358" height="615" alt="Screenshot 2026-08-29 185013" src="https://github.com/user-attachments/assets/c1a10179-c34b-4004-8068-eee8a7928ec7" />
<img width="1074" height="584" alt="Screenshot 2026-08-29 190620" src="https://github.com/user-attachments/assets/17629d7e-2d44-4025-9edf-b750f60e3be8" />
<img width="1055" height="588" alt="Screenshot 2026-08-29 190632" src="https://github.com/user-attachments/assets/20c97a39-2f71-4a70-a2f8-7ebf24fe1488" />
<img width="1362" height="594" alt="Screenshot 2026-08-30 121241" src="https://github.com/user-attachments/assets/765902c2-dae3-4361-b28d-b7856c1ffd6f" />
<img width="1085" height="579" alt="Screenshot 2026-08-30 121921" src="https://github.com/user-attachments/assets/681a4121-6eb7-44e3-994c-f1493933492c" />
<img width="1361" height="585" alt="Screenshot 2026-08-30 122057" src="https://github.com/user-attachments/assets/08487517-d226-4893-8772-51c727a7d79c" />
<img width="1343" height="594" alt="Screenshot 2026-08-30 122115" src="https://github.com/user-attachments/assets/5ba95089-04db-4ee9-99eb-9bad304e91ad" />
