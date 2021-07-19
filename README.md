# copyrightMossChecker

# Check Solution against Submission
1. Make sure that a directory titled solution is in the root 
   folder OR specify the path to the solution code as the first 
   system argument.
2. Make sure that a directory titled submission2 is in the root 
   folder OR specify the path to the submission code as the second 
   system argument.

Note 1: Currently, if you want to specify the path of submission2, you
have to specify the path of the solution. There is no support for
using partial system arguments. It is either all or none.

Note 2: Specify the base files (which files should not be looked at
for plagiarism) in the config.py file. Not all submissions may be the
same. As a result, you may have to manually comment out some lines in
config.py for certain submissions.

Note 3: The system argument solutionTwo specifies to use this particular
comparison for plagiarism, namely... a solution compared to a submission.

Example command using default paths:

python3.9 copyChecker.py solutionTwo

Example command using non-default paths:

python3.9 copyChecker.py solutionTwo ${solution_path} ${submission2_path}

# Check Submission against Submission

# Check Solution against All Submissions

# Check All Submissions against All Sumbissions