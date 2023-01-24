import os, glob, shutil

# function to create output folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

dir_path2 ="D:/data/test/"
dest = "D:/data/final/"

sequence_verio = ["/*tra_caipi3_bh*.nii","/*tra_arterial*.nii","/*venous*.nii","/*tra_delayed*.nii","/*tra_caipi3_bh_DELAYED_20M*.nii"]
output_sequence_name = ["/NE.nii","/AP.nii", "/AP_sub.nii", "/PVP.nii", "/TP.nii", "/HBP.nii"]

for item in os.scandir(dir_path2):
    if item.is_dir():
        src = dir_path2 + item.name
        final_dst = dest + item.name
        createFolder(final_dst)
        j = 0
        for i in sequence_verio:            
            nifti_file = glob.glob(src+i)
            if j == 1:
                shutil.copy(nifti_file[0],final_dst+output_sequence_name[j])
                shutil.copy(nifti_file[1],final_dst+output_sequence_name[j+1])
                j == 3
            else:
                shutil.copy(nifti_file[0],final_dst+output_sequence_name[j])
                j += 1