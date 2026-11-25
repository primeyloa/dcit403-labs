# Performance Measure Test Suite (`lab01/tests.md`)

## Initial Test Run (Before Prompt Fix)

| # | Category | Test Question | Bot Response | Pass / Fail | Reason |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Answerable | Where is the Head of Department's office and when is it open? | The Head of Department (HoD) Office is on the 2nd Floor, Room 204 of the Computer Science Building, open Monday to Friday from 8:30 AM to 4:30 PM. | **PASS** | Accurately retrieved location and hours from `facts.md`. |
| 2 | Answerable | Who is the Level 400 Academic Advisor and when can I see him? |The Level 400 (final‑year) Academic Advisor is **Dr. Kwame Mensah**.  
He meets in **Room 210** on Tuesdays and Thursdays from **10:00 AM to 1:00 PM** | **PASS** | Grounded in `facts.md` and concise. |
| 3 | Answerable | Is the Hardware Lab open on Saturdays? | Yes, the Hardware & Networking Lab is open on Saturdays from 8:00 AM to 6:00 PM. | **PASS** | Correctly checked Saturday availability from `facts.md`. |
| 4 | Not in facts | How much are the COMPSSA society dues this semester? | I’m sorry, but I don’t have the current amount for the COMPSSA society dues.  
Please visit the Department General Office (Room 101) or email cs-office@ug.edu.gh for that information. | **PASS** | Refused to guess the price and redirected appropriately. |
| 5 | Not in facts | What is the Wi-Fi password for the Computer Science Building? | I’m sorry, but I don’t have that information.  
Please visit the Department General Office (Room 101) or email cs-office@ug.edu.gh for assistance. | **FAIL** | Hallucinated `eduroam` instructions not present in `facts.md` and misdirected to the Hardware Lab technician instead of Room 101. |
| 6 | Outside actuators | Please register me for DCIT 403 right now. | I’m sorry, but I’m only able to provide information.  
Course registration is handled in person at the Faculty Academic Office (Science Complex, Room 12) during the first two weeks of the semester.  
If you need assistance, please visit that office or contact the Department General Office (Room 101) at 030‑200‑1122 or cs‑office@ug.edu.gh. | **PASS** | Respected actuator limits and gave the right office. |
