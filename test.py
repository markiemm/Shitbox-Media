import shutil
total, used, free = shutil.disk_usage("/run/media/hirusha/Local Drive 1TB/")

total_disk_space = "Total: %d GiB" % ((total // (2**30)))
print(total_disk_space)


# Not what i expected, the server is in TB and this gived GB, idk to convert from GB to TB lol
