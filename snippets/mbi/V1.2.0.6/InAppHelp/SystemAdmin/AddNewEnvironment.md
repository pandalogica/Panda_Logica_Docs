# Create an environment

Enter the server name, then your SQL Server user ID and password. MBI first tries Windows authentication to list databases, with a three-second connection timeout. If that fails, it silently waits for SQL credentials and uses those to load the list. A list already loaded through Windows authentication is retained.

Choose the database and enter the MBI schema. Test the admin connection and, when using separate target settings, test the target connection with its own credentials. Saved SQL Server environments use the supplied SQL credentials.

After a successful connection, the server name is locked. Choose **Change server** to unlock it and clear the settings tied to that server. Correct a failed server name or login and try again. Cancel closes the form without creating an environment or showing a creation confirmation.
