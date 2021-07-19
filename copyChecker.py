import os
import sys
import subprocess
import io
import time
from select import select
from config import specificCommonFiles

class MossConfig:
    def __init__(self, mossPath):
        self.language = "cc"
        self.commonFiles = specificCommonFiles
        self.mossPath = mossPath
        self.appendage = "core/src/*/*.cpp"

    def setPermissions(self):
        print("Setting executable permissions on the moss script.")
        print("Running command:")
        command = "chmod ug+x " + self.mossPath
        print(command)
        stream = os.popen(command)

    def mossCommand(self, submissionA, submissionB):
        l_flag = "-l " + self.language
        d_flag = "-d"
        b_flags = ""
        prependSubmissionA = submissionA + "/"
        prependSubmissionB = submissionB + "/"
        for file in self.commonFiles:
            b_flags += " -b " + prependSubmissionA + file
            b_flags += " -b " + prependSubmissionB + file
        return self.mossPath + " " + l_flag + \
               b_flags + " " + d_flag + " " + \
               submissionA + "/" + self.appendage + \
               " " + submissionB + "/" + self.appendage

    def mossCommandList(self, submissionA, submissionB):
        l_flag = "-l " + self.language
        d_flag = "-d"
        b_flags = []
        prependSubmissionA = submissionA + "/"
        prependSubmissionB = submissionB + "/"
        for file in self.commonFiles:
            b_flags.append("-b " + prependSubmissionA + file)
            b_flags.append("-b " + prependSubmissionB + file)
        d_flag = "-d" + " " + \
               submissionA + "/" + self.appendage + \
               " " + submissionB + "/" + self.appendage
        return [self.mossPath, l_flag] + b_flags + [d_flag]


    def compare(self, submissionA, submissionB):
        command = self.mossCommand(submissionA, submissionB)
        print("Comparing " + submissionA + " and " + submissionB)
        print("Running command:")
        print(command)
        process = subprocess.Popen(command, shell=True)
        # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        # parseProcessStdOut(process)

    def parseProcessStdOut(self):
        pass
        # lastLine = ""
        # time.sleep(2)
        # stdout = process.stdout.decode('utf-8')
        # for line in iter(stdout.readline, ''):
        #     print(line)
        #     lastLine = line.rstrip()
        # print(lastLine)
        # while process.poll() is None:
        #     # print('returncode is', p.returncode)
        #     available_readers = select([process.stdout, process.stderr], [], [], 2.0)[0]
        #     for r in available_readers:
        #         print(r.read(1), end='')
        # while process.returncode is None or process.stdout.closed:
        #     # print('returncode is', p.returncode)
        #     for line in iter(process.stdout.readline, ''):
        #         print(line)

def parseSubmissionsDirectory(arg):
    submissionDirectory = "./submissions"
    try:
        submissionDirectory = arg[0]
        print("Submission directory specified. Using submission "
              "directory: " + submissionDirectory)
    except IndexError:
        print("Submissions directory not specified. Attempting to use"
              "default submission directory: ./submissions")
    return submissionDirectory


def parseMossPath(arg):
    mossPath = "./moss"
    try:
        mossPath = arg[1]
        print("Moss path specified. Using moss path: " + mossPath)
    except IndexError:
        print("Moss path not specified. Attempting to use"
              "default moss path: ./moss")
    return mossPath


def compareAll(argv):
    directory = parseSubmissionsDirectory(argv)
    mossPath = parseMossPath(argv)
    submissions = [f.path for f in os.scandir(directory) if f.is_dir()]
    mossConfig = MossConfig(mossPath)
    mossConfig.setPermissions()
    for submissionA in submissions:
        for submissionB in submissions:
            if submissionA != submissionB:
                mossConfig.compare(submissionA, submissionB)

def compareTwo(argv):
    directory1 = parseSubmissionsDirectory(argv)
    directory2 = parseSubmissionsDirectory(argv)
    mossPath = parseMossPath(argv)
    submissions = [f.path for f in os.scandir(directory) if f.is_dir()]
    mossConfig = MossConfig(mossPath)
    mossConfig.setPermissions()
    for submissionA in submissions:
        for submissionB in submissions:
            if submissionA != submissionB:
                mossConfig.compare(submissionA, submissionB)
                return

def compareSolutionAll(argv):
    pass

def compareSolutionTwo(argv):
    pass

if __name__ == "__main__":
    if sys.argv[1] == "two":
        print("Two option selected. Only comparing two submissions.")
        compareTwo(sys.argv[2:])
    elif sys.argv[1] == "solutionAll":
        compareSolutionAll(sys.argv[2:])
    elif sys.argv[1] == "solutionTwo":
        compareSolutionTwo(sys.argv[2:])
    else:
        print("Comparing all submissions.")
        compareAll(sys.argv[2:])
