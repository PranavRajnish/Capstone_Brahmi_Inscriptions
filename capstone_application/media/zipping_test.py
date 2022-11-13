import shutil
import os

dir_path = 'C:\\MyStuff\\PES\\Capstone_Application\\capstone_application\\media\\images\\' + 'freeme'
result_path = 'C:\\MyStuff\\PES\\Capstone_Application\\capstone_application\\media' + '\\results\\' + 'freeme2' +"_results"

print(dir_path)
print(result_path)
shutil.make_archive(result_path, "zip", dir_path)