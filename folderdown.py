from ftplib import FTP,error_perm
import os, sys,time




listfolder=[]

def walk_dir(f, server_path):
    original_dir = f.pwd()
    try:
        f.cwd(server_path)
    except error_perm:
        return  
    #print dirpath
    listfolder.append(server_path)
    names = f.nlst()
    for name in names:
        walk_dir(f, server_path + '/' + name)
    f.cwd(original_dir)  
def create_folder(client_path):
    x=0
    while x<len(listfolder):
        if not os.path.exists(client_path+listfolder[x]):
            os.makedirs(client_path+listfolder[x])
            #print "basarili"
        x=x+1
def copy_files(f,path_client):
    x=0
    while x<len(listfolder):
        f.cwd(listfolder[x])
        a=f.nlst()
        for i in a:
            try:
                file_name=i
                file_path=path_client+listfolder[x]+"/"+i
                filee=open(file_path,'wb')
                f.retrbinary('RETR %s'%file_name,filee.write)
            except:
                pass
            
        f.cwd('/')
        print f.pwd()
        x=x+1
#server folder must call with 'path to folder/will be copied folder'
def main_function(server_path,client_path,ftp_url,user_name,password):
    ftp = FTP(ftp_url)
    ftp.login(user_name, password)
    listfolder=[]
    server_folder=server_path
    walk_dir(ftp, server_folder)
    print listfolder
    #create folder argument is client side path where will be copied on client side.
    create_folder(client_path)
    copy_files(ftp,client_path)
    ftp.quit()
#for example delete all '#'s 
#main_function("/cafe","C:/",'127.0.0.1',"user","12345")
#time.sleep(1)
#main_function("/sss","C:/",'127.0.0.1',"user","12345")
