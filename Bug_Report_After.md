\# Bug Report – Scanner App Crashes on Invalid Barcode (AI‑Enhanced)



| Field | Details |

|-------|---------|

| \*\*Title\*\* | App crashes when scanning an invalid barcode (all 9s) |

| \*\*App Version\*\* | 1.23.0 (build 42) |

| \*\*Device\*\* | Realme RMXXX, Android 13 (non‑rooted) |

| \*\*Severity\*\* | Major (app becomes unusable) |

| \*\*Priority\*\* | High (affects core scanning workflow) |

| \*\*Environment\*\* | Production, real device, Wi‑Fi on |



\### Steps to Reproduce

1\. Launch the Open Food Facts Scanner app.  

2\. Point the camera at an invalid barcode: `9999999999999`.  

3\. Wait for the app to attempt product lookup (2–3 seconds).  



\### Actual Result

The app crashes and closes to the home screen. No error message is shown.  



\### expected Result

The app should display a user‑friendly message: \*"Product not found. Please try a different barcode."\* and remain responsive.  



\### Additional Information

\- \*\*Reproducibility:\*\* 5/5 attempts.  

\- \*\*Network:\*\* Stable Wi‑Fi (100 Mbps).  

\- \*\*Logs:\*\* No crash log available; Android `logcat` shows `NullPointerException` in `ProductLookupService`.  



\### Suggested Root Cause

The backend API returns a `404` for invalid barcodes, but the app does not handle the null response gracefully.  



\### Recommended Fix

Wrap the API response handling in a try‑catch block. If product is null, show a toast instead of crashing.  



\### AI Contribution

This report was improved using ChatGPT for structure, completeness, and root cause hypothesis. Original report (before AI) is available.



\*\*Reported by:\*\* QA

\*\*Date:\*\* 2026-04-22

