# gpgBruteForce
Simple python script to brute force the password for files that were encrypted with ```gpg -c```. 

Attempts approximately 100 passwords per second. 

# Warning

Do not run on untrusted user input. All passwords are used in a shell command without escaping so it would be trivial to get code execution from a password. 

This is *very* unoptimized. This does not do anything more than try to decrypt the file with gpg. 
 
