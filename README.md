# 🚆 KPA API Assignment – FastAPI Implementation

This project is a backend implementation of selected APIs from the KPA Form Data assignment using **FastAPI** and **PostgreSQL**.

---

## ✅ 1) Setup Instructions

Follow these steps to set up and run the project locally:

### 🔧 Environment Setup

1. **Clone or download** the project folder.
         git clone https://github.com/N1shkarsh-70/kpa.git
2. **Create and activate a virtual environment**:
   python -m venv menv
   # Windows
   menv\Scripts\activate
   
3. **Install the dependencies**:
   
   pip install -r requirements.txt
   
4. **Set up the `.env` file** in the root directory:
   
   DATABASE_URL=postgresql://postgres:YourPassword@localhost:5432/kpa_assignment


5. **Create the PostgreSQL database**:
   - Open pgAdmin or terminal and run:
     
     CREATE DATABASE kpa_assignment;

6. **Run the FastAPI app**:
   
   uvicorn app.main:app --reload
   

7. **Test the APIs**:
   - Open Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Or use Postman with your exported collection.

---

## 2) Tech Stack Used
- **FastAPI**

- **PostgreSQL**

- **SQLAlchemy**

- **Uvicorn**

- **Dotenv**

---

## 3) List of Implemented APIs and Their Descriptions

### 1. **POST /api/forms/wheel-specifications**

-  **Function**: Submits a new wheel specification form.
-  **Request Fields**: `formNumber`, `submittedBy`, `submittedDate`, and `fields` (JSON object).
-  **Returns**: Confirmation with saved form metadata.
   **Response**:
      {
         "success": true,
         "message": "Wheel specification submitted successfully.",
         "data": {
            "formNumber": "WHEEL-2025-001",
            "submittedBy": "user_id_123",
            "submittedDate": "2025-07-03",
            "status": "Saved"
         }
      }
---

### 2. **POST /api/forms/bogie-checksheet**

- 📥 **Function**: Submits bogie inspection data including three sections:
  - `bogieDetails`
  - `bogieChecksheet`
  - `bmbcChecksheet`
-  **Returns**: Confirmation with form number, inspector ID, and status.
-  **Response**:
      {
         "success": true,
         "message": "Bogie checksheet submitted successfully.",
         "data": {
            "formNumber": "BOGIE-2025-001",
            "inspectionBy": "user_id_456",
            "inspectionDate": "2025-07-03",
            "status": "Saved"
         }
      }         
---

### 3. **GET /api/forms/wheel-specifications**

- **Function**: Retrieves wheel specification forms based on query filters.
- **Query Params**: `formNumber`, `submittedBy`, `submittedDate`
- **Returns**: A list of matching forms and their stored field data.
- **Response**:
      {
         "success": true,
         "message": "Filtered wheel specification forms fetched successfully.",
         "data": [
            {
                  "submittedBy": "user_id_123",
                  "fields": {
                     "treadDiameterNew": "915 (900-1000)",
                     "lastShopIssueSize": "837 (800-900)",
                     "condemningDia": "825 (800-900)",
                     "wheelGauge": "1600 (+2,-1)",
                     "variationSameAxle": "0.5",
                     "variationSameBogie": "5",
                     "variationSameCoach": "13",
                     "wheelProfile": "29.4 Flange Thickness",
                     "intermediateWWP": "20 TO 28",
                     "bearingSeatDiameter": "130.043 TO 130.068",
                     "rollerBearingOuterDia": "280 (+0.0/-0.035)",
                     "rollerBearingBoreDia": "130 (+0.0/-0.025)",
                     "rollerBearingWidth": "93 (+0/-0.250)",
                     "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
                     "wheelDiscWidth": "127 (+4/-0)"
                  },
                  "formNumber": "WHEEL-2025-001",
                  "submittedDate": "2025-07-03"
            }
         ]
      }