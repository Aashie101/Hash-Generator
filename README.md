File Integrity Checker using SHA-256
Overview

This project demonstrates a simple file integrity verification system using Python and the SHA-256 hashing algorithm.

The project consists of two scripts:
- hashgenerator.py – Generates a SHA-256 hash of a file and stores it in hash.txt.
- verify.py – Verifies whether a file has been modified by comparing its current hash with the stored hash.

This is a basic cybersecurity project that introduces the concepts of:
1. Cryptographic Hash Functions
2. File Integrity Monitoring
3. SHA-256 Hashing
4. Tamper Detection

**How It Works**
**Step 1: Generate Hash**

The hashgenerator.py script:

Reads important.txt
Calculates its SHA-256 hash
Stores the following information in hash.txt:
File name
Hash value

Example:

important.txt
4c8d7f0e4d5b1f2c6d3e8a9b...

**Step 2: Verify File**

The verify.py script:

Reads the original file name and hash from hash.txt
Asks the user for a file to check
Calculates the SHA-256 hash of the supplied file
Compares it with the stored hash

Possible results:

File is Safe
File: important.txt
file is safe
Different File
Different files

Occurs when the user enters a file name different from the one originally hashed.

File Modified
Danger: file modified

Occurs when the file contents have changed since the hash was generated.
