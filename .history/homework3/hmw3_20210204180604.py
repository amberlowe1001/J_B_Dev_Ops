Lesson 3. Homework Assignment
1.	Pseudo devices
a.	Where in a Linux system will you look for device files? –
i. / dev
b.	What pseudo device is generates zeroes
i. / dev/zero
c.	What pseudo device is a blackhole
i. / dev/null
d.	What devices are generate random characters
i. / dev/random
2.	Hardware Devices
a.	What device is usually carrying a root filesystem?
i. / root
b.	You already have a root volume and one data volume attached, and you just attached one more volume to the system. What device name this volume will most likely have?
i. / dev/xvda or /dev/xvdf / data
3.	Filesystem
a.	What would be a linux command for creating xfs filesystem on a attached device
i.	Mkfs.xfs/dev/
4.	Hidden files
a.	Why hidden files exists
i.	These files are necessary for the operation system and keeping them hidden will protect them from accidental deletion
b.	How to list all hidden files in Home directory
i.	Ls - a/home/
5.	Linux user data
a.	You have a task to write a script that will archive all  users data on a Linux host. Where will you  be looking for a list of folders to archive?
i. / usr .bash_logout
6.	Temporary and virtual folders.
a.	You have a task to write a script that will archive/backup all data on a Linux host. What folders from the 1st level of the root filesystem are you going to add to an exclusion list?
i. / dev/tempfs/archive/backup
Optional:
7.	Practice assignment
a.	Create VM in GCP. Use a CentOS7 image with additional volume.
b.	Connect to the host with ssh
c.	Create single primary partition on the non-root volume
d.	Format the partition to xfs
e.	Create folder `/ mount/mydata`
f.	Mount the partition to `/ mount/mydata` folder
g.	Check linux disks layout with `dh - h`
h.	Update fstab file to have it automounted
8.	Permissions. Please provide exact linux command that will do requested permission on `/ tmp/mytestfile`
a.	Set read only for all users
i.	Chmod 644 / tmp/mytestfile // owner can Read and Write, others can Read
b.	Set read, write and execute permission for file owner only
i.	Chmod 600 / tmp/mytestfile // Only Owner can Read and Write
c.	Revoke only execute permission
i.	Chmod - wx / tmp/mytestfile
d.	Revoke write permission for group
e.	Chmod 750 / tmp/mytestfile
