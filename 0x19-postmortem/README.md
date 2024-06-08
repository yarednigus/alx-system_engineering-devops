Duration of the Outage:

Start: June 7, 2024, 14:00 UTC
End: June 7, 2024, 16:30 UTC
Impact:

The user authentication service was down, preventing users from logging into the application.
Approximately 80% of users were affected, experiencing failed login attempts.
Root Cause:

The root cause was an expired SSL certificate used by the authentication server, which caused secure connections to fail.
Timeline
14:05 UTC: Issue detected via monitoring alert indicating a high rate of login failures.
14:10 UTC: Incident confirmed by support engineer after verifying user reports.
14:15 UTC: Initial investigation focused on database connectivity, suspecting a potential issue with user data retrieval.
14:25 UTC: Database team reported no issues; investigation shifted to network configurations and server logs.
14:45 UTC: Identified SSL certificate error in server logs indicating expired certificate.
15:00 UTC: Incident escalated to DevOps team for certificate renewal.
15:30 UTC: DevOps team confirmed the certificate had expired and initiated renewal process.
16:00 UTC: New SSL certificate installed and tested.
16:15 UTC: Monitoring confirmed resolution of the issue with successful login attempts.
16:30 UTC: Full service restored and incident closed.
Root Cause and Resolution
Root Cause:

The SSL certificate on the authentication server expired, leading to the failure of secure connections necessary for the authentication process. The automated renewal process failed due to a configuration error in the certificate management system, causing the expiration to go unnoticed.
Resolution:

The expired SSL certificate was manually renewed by the DevOps team. Post-renewal, the authentication server was restarted to apply the new certificate. Thorough testing confirmed that secure connections were successfully re-established, and users could log in without issues.
Corrective and Preventative Measures
Improvements/Fixes:

Implement automated notifications for upcoming SSL certificate expirations.
Review and correct the configuration in the certificate management system to ensure automated renewals are correctly processed.
Enhance monitoring to include SSL certificate validity checks.
Task List:

Patch the certificate management system to fix the configuration error.
Set up automated alerts for SSL certificate expiration dates.
Add SSL certificate validity checks to the regular monitoring routines.
Conduct a training session for the DevOps team on managing SSL certificates and handling renewals.
Schedule periodic audits of SSL certificates to ensure compliance and validity.
This structured approach will help in preventing similar issues in the future and ensure a more resilient and robust authentication service.






