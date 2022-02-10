import os
import dropbox
class TransferData():
    def __init__(self,access_token) :
       self.access_token = access_token
    
    def upload_file(self,file_from,file_to) :
       dbx = dropbox.Dropbox(self.access_token)
       for root,folders,files in os.walk(file_from):
           for fileName in files :
               local_path = os.path.join(root,fileName)
               relative_path = os.path.relpath(local_path,file_from)
               dropbox_path = os.path.join(file_to,relative_path)
               with open(local_path,"rb") as f :
                   dbx.files_upload(f.read(),dropbox_path,mode = dropbox.files.WriteMode.overwrite)

def main():
    access_token = 'sl.BBwLP3LxwCNrzldWYKGFtfXGi-QSEDTbo5XskmPsbFsIQRHtE4pFQ0rkLVQwlyannvIVhl0hb4nCfnkvM1DYii9qPXpuhPU_9gN34JAJCsMxyCnfWd3kacDEVPJ9XhUzaqGiABU'
    transferData = TransferData(access_token)
    file_from = str(input("enter the path which you need to upload : "))
    file_to = "/Python_Code/" # The full path to upload the file to, including the file name
    transferData.upload_file(file_from, file_to)
    print("file uploaded sucessfully on cloud")

main()
    
