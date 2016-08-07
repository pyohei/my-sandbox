#!/usr/local/bin/python
# -*- coding: utf-8 -*-


"""

"""

import os
import uploader_conf

CONNECTION_MAP = {
    1: "scp",
    2: "ftp"
}

class Connection(object):

    def __init__(self):
        self.connection = self.__connect()

    def __connect(self):
        if uploader_conf.CONNECTION_TYPE == 1:
            return SCP()
        if uploader_conf.CONNECTION_TYPE == 2:
            return FTP()

    def get_connection(self):
        return self.connection

    def has_dir(self, dir_path):
        return self.connection.has_dir(dir_path)

    def has_file(self, file_path):
        return self.connection.has_file(file_path)

    def upload(self, local_path, remote_path):
        self.connection.upload(local_path, remote_path)

    def close(self):
        self.connection.close()

class SCP(object):

    def __init__(self):
        self.connection = None
        self.sftp = None
        self.host = uploader_conf.SCP_HOST
        self.port = uploader_conf.SCP_PORT
        self.username = uploader_conf.SCP_USERNAME
        self.password = uploader_conf.SCP_PASSWORD
        self.__connect()

    def __connect(self):
        import paramiko
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn.connect(
            self.host,
            port = self.port,
            username = self.username,
            password = self.password
            )
        self.connection = conn
        self.sftp = conn.open_sftp()

    def has_dir(self, dir_path):
        self.sftp.chdir("/")
        try:
            self.sftp.chdir(dir_path)
            self.sftp.chdir("/")
            return True
        except:
            return False

    def has_file(self, file_path):
        filename = os.path.basename(file_path)
        dirname = os.path.dirname(file_path)
        try:
            filenames = self.sftp.listdir(dirname)
            if filename in filenames:
                return True
        except:
            return False

    def upload(self, local_path, remote_path):
        self.sftp.put(local_path, remote_path)

    def close(self):
        self.sftp.close()
        self.connection.close()

class FTP(object):

    def __init__(self):
        self.ftp = None
        self.host = uploader_conf.FTP_HOST
        self.port = uploader_conf.FTP_PORT
        self.username = uploader_conf.FTP_USERNAME
        self.password = uploader_conf.FTP_PASSWORD
        self.__connect()

    def __connect(self):
        from ftplib import FTP
        self.ftp = FTP(self.host, self.username, self.password)

    def has_dir(self, dir_path):
        self.ftp.cwd("/")
        try:
            self.ftp.cwd(dir_path)
            self.ftp.cwd("/")
            return True
        except:
            return False

    # undifine method. This is copied by class `SCP`
    def has_file(self, file_path):
        filename = os.path.basename(file_path)
        dirname = os.path.dirname(file_path)
        try:
            filenames = self.ftp.nlst(dirname)
            if filename in filenames:
                return True
        except:
            return False

    def upload(self, local_path, remote_path):
        f = open(local_path, "rb")
        command = "STOR " + remote_path
        self.ftp.storbinary(command, f)

    def close(self):
        self.ftp.close()
        self.ftp.quit()

if __name__ == "__main__":
    pass
