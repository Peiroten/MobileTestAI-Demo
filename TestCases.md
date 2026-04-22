\# Test Cases – Open Food Facts Scanner App



\*\*Author:\*\* Raul Peiroten  

\*\*Date:\*\* April 2026  

\*\*App:\*\* Open Food Facts Scanner (`org.openfoodfacts.scanner`)  



Test cases for functional, negative, edge, and non‑functional testing techniques. They demonstrate systematic QA thinking.



\---



\## Functional Test Cases (Happy Path \& Variations)



| # | Test Case | Expected Result |

|---|-----------|------------------|

| 1 | Scan a valid EAN‑13 barcode (e.g., 3017620425035 – Nutella) | App identifies product, displays name and nutrition grade. |

| 2 | Scan a valid UPC‑A barcode (12 digits) | App recognizes as valid, shows product info. |

| 3 | Scan a product that exists in offline cache (no internet) | App shows cached data (if previously scanned) or displays "offline" message. |

| 4 | Manually enter a barcode via keyboard (if supported) | App processes the number and shows correct product. |

| 5 | Scan the same barcode twice in a row | App does not duplicate the product in history; shows existing entry. |



\---



\## Negative Test Cases (Error Handling)



| # | Test Case | Expected Result |

|---|-----------|------------------|

| 6 | Scan an invalid barcode (e.g., 123456) | App shows "Product not found" or error message, does not crash. |

| 7 | Scan a barcode of a non‑food item (e.g., book ISBN) | App either shows no data or gracefully indicates "not in database". |

| 8 | Scan with camera permission denied | App requests permission again or shows instruction to enable it. |

| 9 | Scan while airplane mode is on (no network) | App attempts to scan, then shows a clear network error (not an infinite spinner). |



\---



\## edge Cases (boundary \& Unusual Conditions)



| # | Test Case | Expected Result |

|---|-----------|------------------|

| 10 | Barcode has extra spaces before/after (if manual entry) | App trims spaces and still matches the product. |

| 11 | Scan a barcode while receiving an incoming phone call | The scan is interrupted; after call ends, app resumes without crash. |

| 12 | Camera is already used by another app (e.g., Instagram open in background) | App acquires camera successfully or shows a clear "camera busy" error. |

| 13 | Scan a very low‑quality barcode (blurry, scratched) | App either fails gracefully or uses auto‑focus to retry; no freeze. |



\---



\## Non‑functional / Usability \& Performance



| # | Test Case | Expected Result |

|---|-----------|------------------|

| 14 | Time to recognize a valid barcode in good light | ≤ 2 seconds (measure manually – acceptable threshold). |

| 15 | App behaviour when device is in low battery mode (Android power saver) | Scanning still works, but camera preview may dim; no crash. |



\---



\## Testing Notes



\- These cases focus on the \*\*scanning workflow\*\* of the app.

\- Real device testing (non‑rooted Android 13) was used.

\- Additional tests could include: history screen, settings, and deep links.



\*\*Key takeaway:\*\* A QA engineer thinks beyond the happy path – covering interruptions, device states, and real‑world user behaviour.

