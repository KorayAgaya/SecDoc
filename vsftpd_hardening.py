#!/usr/bin/python

import fileinput
from shutil import copyfile

print("vsftp_hardening baslatiliyor.")

copyfile("/etc/vsftpd.conf", "/etc/vsftp.conf.old")

for line in fileinput.input('vsftpd.conf', inplace=True):
      print line.rstrip().replace('#write_enable=YES', 'write_enable=YES')
for line in fileinput.input('vsftpd.conf', inplace=True):
      print line.rstrip().replace('#chroot_local_user=YES', 'chroot_local_user=YES')
for line in fileinput.input('vsftpd.conf', inplace=True):
      print line.rstrip().replace('#ftpd_banner=Welcome to blah FTP service.', 'FTP Server.')
for line in fileinput.input('vsftpd.conf', inplace=True):
      print line.rstrip().replace('#xferlog_std_format=YES', 'xferlog_std_format=NO')

print("vsftpd_hardening islem tamamlandi. Eski yapilandirma dosyasi /etc/vsftpd.conf.old olarak kaydedildi.")
