import os
import sys

class MossConfig:
    def __init__(self, mossPath):
        self.language = "cc"
        self.commonFiles = ["exampleDir/a.cc", "exampleDir/d.h"]
        self.mossPath = mossPath
        self.appendage = "*.cc"

    def setPermissions(self):
        print("Setting executable permissions on the moss script.")
        print("Running command:")
        command = "chmod ug+x " + self.mossPath
        print(command)
        stream = os.popen(command)
        print(stream)

    def mossCommand(self, submissionA, submissionB):
        l_flag = "-l " + self.language
        d_flag = "-d"
        b_flag = ""
        prependSubmissionA = submissionA + "/"
        prependSubmissionB = submissionB + "/"
        for file in self.commonFiles:
            b_flag += " -b " + prependSubmissionA + file
            b_flag += " -b " + prependSubmissionB + file
        return self.mossPath + " " + l_flag + \
               b_flag + " " + d_flag + " " + \
               submissionA + "/" + self.appendage + \
               " " + submissionB+ "/" + self.appendage


def compare(submissionA, submissionB, mossConfig):
    command = mossConfig.mossCommand(submissionA, submissionB)
    print("Comparing " + submissionA + " and " + submissionB)
    print("Running command:")
    print(command)
    stream = os.popen(command)

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


def main(argv):
    directory = parseSubmissionsDirectory(argv)
    mossPath = parseMossPath(argv)
    submissions = [f.path for f in os.scandir(directory) if f.is_dir()]
    mossConfig = MossConfig(mossPath)
    mossConfig.setPermissions()
    for submissionA in submissions:
        for submissionB in submissions:
            if submissionA != submissionB:
                compare(submissionA, submissionB, mossConfig)
                return


if __name__ == "__main__":
    main(sys.argv[1:])
