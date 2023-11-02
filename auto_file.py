import subprocess
import fileinput
import sys

 
nr_stiffness_ratio = ["3","5"]
nr_growth_ratio = ["2","3"]


for growth_ratio in nr_growth_ratio:
    for stiffness_ratio in nr_stiffness_ratio:
        print ("===================================================================================================================")
        print ("\n Stiffness rate "+stiffness_ratio+" ,growth ratio "+growth_ratio+"\n")
        print ("===================================================================================================================")
        for line in fileinput.input("Parameters.prm", inplace=1):
            if "set The ratio of stiffness" in line:
                line = "        set The ratio of stiffness                       = "+stiffness_ratio+" \n"
            if "set  Growth ratio"in line:
                line = "        set  Growth ratio                                = "+growth_ratio+" \n"
            sys.stdout.write(line)

        
        a = subprocess.run(['sudo', './Brain_growth', 'Parameters.prm',  sys.argv[1]])
            
        folder_name = "SR" + stiffness_ratio +"_GR" + growth_ratio
        makefolder = subprocess.Popen('sudo mkdir    '+folder_name, shell=True)
        makefolder.wait()
        copy1 = subprocess.Popen('sudo cp  Output*          '+folder_name, shell=True)
        copy1.wait()
        copy2 = subprocess.Popen('sudo cp  Parameters.prm     '+folder_name, shell=True)
        copy2.wait()
        copy3 = subprocess.Popen('sudo cp  timeing.csv     '+folder_name, shell=True)
        copy3.wait()
        remove = subprocess.Popen('sudo rm  Output*  timeing.csv      ', shell=True)
        remove.wait()
        print ("COPY DONE! \n")

