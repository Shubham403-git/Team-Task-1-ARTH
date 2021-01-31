import os
import pyttsx3
import wikipedia
import subprocess as sp
import datetime
import time
import webbrowser
from datetime import date
import speech_recognition as sr
pyttsx3.speak("Tell me your requirments:")
print("*******Supports only local login till now******\n******Remote login coming soon******")
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.enery_threshold = 4000
        r.adjust_for_ambient_noise(source, duration =3)
        print('We Are Listening..........')
        audio=r.listen(source)
        print('Speech Done.')
    try:
        p=r.recognize_google(audio)
    except sr.UnknownValueError:
        pyttsx3.speak("Sorry, I didn't get that . Please try again")
        continue
    except sr .RequestError.with_traceback:
        pyttsx3.speak("Sorry, I didn't get that . Please try again")
        continue
    q=(('run' in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ('connect' in p)) or ('launch' in p) or ('create' in p)or ('make' in p) 
    if (('do not' in p )or ('do nothing' in p) or ("don't" in p) or ('never' in p)):
        print('ok as your wish')
        pyttsx3.speak('ok as your wish')
        continue
    elif ("exit" in p) or ("quit" in p) or ("terminate" in p) or ("end" in p):
        print("Thanks, see yoy again.")
        pyttsx3.speak("Thanks, see yoy again.")
        break
######################################################################## HADOOP #####################################################################

    elif (("install" in p)or("download" in p)) and ("hadoop" in p):
	pyttsx3.speak('Installing Hadoop')
	os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm --force")
	pyttsx3.speak('Successfully installed')
	print("Successfully installed")

    elif (("install" in p)or("download" in p)) and ("java" in p):
	pyttsx3.speak('Installing java')
	os.system("rpm -i jdk-8u171-linux-x64.rpm")
	pyttsx3.speak('Successfully installed')
	print("Successfully installed")

    #Namenode configuration
    elif ("configure" in p) and (("hadoop" in p)or("masternode" in p)or("namenode" in p)):
	#check wheather required softwares are installed or not
	p=os.system("which hadoop")
	q=os.system("which java")
	if(p!=0):
		print("Error: Hadoop not found")
		pyttsx3.speak('Hadoop not found')
		ans=input("Do you want to install hadoop[Y/N]: ")
		pyttsx3.speak('Do you want to install hadoop')
		if(ans=="Y"):
			os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm --force")
		else:
			print("Ending.....")
			exit()
	if(q!=0):
		print("Error: Java not found")
		ans=input("Do you want to install jdk[Y/N]: ")
		if(ans=="Y"):
			os.system("rpm -i jdk-8u171-linux-x64.rpm")
		else:
			print("Ending.....")
			exit()

	master_ip=input("Enter the ip address of MasterNode/NameNode: ")
	pyttsx3.speak('configuring master node')

	#configuring hdfs-site.xml file
	text='''<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/nn</value>\n</property>\n</configuration>'''
	Dfile_hdfs=open("/etc/hadoop/hdfs-site.xml","w")
	Dfile_hdfs.write(text)
	Dfile_hdfs.close()

	#configuring core-site.xml file
	text='''<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs:{}:9001</value>\n</property>\n</configuration>'''
	Dfile_core=open("/etc/hadoop/core-site.xml","w")
	Dfile_core.write(text.format(master_ip))
	Dfile_core.close()
		
	#formatting namenode
	os.system("hadoop namenode -format -y")
	print("Successfully configured...:)")
	pyttsx3.speak('Successfully configured')

    #Datanode configuration
    elif ("configure" in p) and (("hadoop" in p)or("slavenode" in p)or("datanode" in p)):
	#check wheather required softwares are installed or not
	p=os.system("which hadoop")
	q=os.system("which java")
	if(p!=0):
		print("Error: Hadoop not found")
		ans=input("Do you want to install hadoop[Y/N]: ")
		if(ans=="Yes"):
			os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm --force")
		else:
			print("Ending.....")
			exit()
	if(q!=0):
		print("Error: Java not found")
		ans=input("Do you want to install jdk[Y/N]: ")
		if(ans=="Yes"):
			os.system("rpm -i jdk-8u171-linux-x64.rpm")
		else:
			print("Ending.....")
			exit()

	master_ip=input("Enter the ip address of MasterNode/NameNode: ")
	pyttsx3.speak('configuring slave node')

	#configuring hdfs-site.xml file
	text='''<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/dn</value>\n</property>\n</configuration>'''
	Dfile_hdfs=open("/etc/hadoop/hdfs-site.xml","w")
	Dfile_hdfs.write(text)
	Dfile_hdfs.close()

	#configuring core-site.xml file
	text='''<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.data</name>\n<value>hdfs:{}:9001</value>\n</property>\n</configuration>'''
	Dfile_core=open("/etc/hadoop/core-site.xml","w")
	Dfile_core.write(text.format(master_ip))
	Dfile_core.close()
		
	print("Successfully configured...:)")
	pyttsx3.speak('Successfully configured')

    #start namenode
    elif ("hadoop" in p)and("start" in p)and("master" in p)or("name" in p):
        pyttsx3.speak('starting namenode')
        os.system('hadoop-daemon.sh start namenode')
        pyttsx3.speak("namenode has started")
            
    #start datanode       
    elif("hadoop" in p)and("start" in p)and("slave" in p)or("data" in p):
        pyttsx3.speak("starting namenode")
        os.system("hadoop-daemon.sh start namenode")
        pyttsx3.speak("datanode has started")


##################################################################################### HADOOP ######################################################################

      #creating key-pair:aws cloud
    elif (('create' in p ) or ('make' in p) and ('key' in p)) :
        print('Enter key name to create :-  ', end='')
        key_name=input()
        o = sp.getstatusoutput('aws ec2 create-key-pair --key-name {}'.format(key_name))
        print(o[1])
	#creating security-group: aws cloud
    elif (('create' in p ) or ('make' in p) and ('security' in p )and ('group'in p)):
        sg_name=input('Enter Security Name :-  ')
        vpc_id=input('Enter VPC Id :-  ')
        os.system('aws ec2 create-security-group --group-name {} --description "SG Created" --vpc-id {}'.format(sg_name , vpc_id))
	#addig ingress rule to security-group:aws cloud
    elif (('Add'in p )or ('make' in p )or ('create' in p)and('Ingress' in p) and ('Security' in p)):
        sg_id=input('Enter Security Group Id :-  ')
        ip_protocol=input('Enter IP Protocol ( ie. tcp ) :-  ')
        port_no=input('Enter Port No :-  ')
        cidr=input('Input Ip Ranges :-  ')
        o= sp.getstatusoutput('aws ec2 authorize-security-group-ingress --group-id {} --ip-permissions IpProtocol={},FromPort={},ToPort={},IpRanges=[{}]'.format(sg_id , ip_protocol , port_no , port_no , cidr))
        print(o[1])
	#Launching Instance on aws cloud
    elif ((q in p ) and ('ec2' in p) or('instance' in p)):
        ami=input('Enter AMI id to Launch Instance :-  ')
        itype=input('Enter Instance type :-  ')
        count=input('Enter Number of Instances to launch :-  ')
        sg_id=input('Enter Security Group Id to attach to the Instance :-  ')
        key=input('Enter Key to attach to ec2 Instance :-  ')
        o=sp.getstatusoutput('aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id subnet-24bcb44c  --security-group-ids {} --key-name {}'.format(ami , itype , count , sg_id , key))
        print(o[1])
	#creating ebs volume
    elif ((q in p) and ('ebs' in p) and ('volume' in p)):
        az=input('Enter Availablity Zone to Create EBS Volume :-  ')
        ebs_size=input('Enter Size to create EBS Volume :-  ')
        o=sp.getstatusoutput('aws ec2 create-volume --availability-zone {} --size {}'.format(az , ebs_size))
        print(o[1])
	#attaching ebs volume to ec2-instance:awsel
    if (('attach'in p) and('ebs' in p) or('volume' in p)):
        ebs_vid=input('Enter EBS Volume ID to Attach to EC2 Instance :-  ')
        ec2_id=input('Enter EC2 Instance ID to attach EBS Volume :-  ')
        o=sp.getstatusoutput('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf'.format(ebs_vid , ec2_id))
        print(o[1])
	#configuring webser on ec2-instance:aws
    elif ('configure' in p) and('webserver'in p) and('ec2'in p)or('instnace' in p):
        remote_ip=input('Enter Ip Address :-  ')
        key=input('Enter key name to login inside Ec2 Instance :-  ')
        o=sp.getstatusoutput('ssh -l ec2-user {} -i {}.pem sudo yum install httpd -y'.format(remote_ip , key))
        print(o[1])
        l=sp.getstatusoutput('ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd'.format(remote_ip , key))
        print(l[1])
        m=sp.getstatusoutput('ssh -l ec2-user {} -i {}.pem sudo systemctl enable httpd'.format(remote_ip , key))
        print(m[1])
	#creating S3 Bucket
    elif (q in p) and ('s3' in p):
        s3_name=input('Enter S3 bucket name that must be unique :-  ')
        o=sp.getstatusoutput('aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1'.format(s3_name))
        print(o[1])
	#putting object inside S3 bucket and with public access
    elif ('put' in p )or('object' in p) and ('s3' in p):
        object_name=input('Enter Object name to put inside S3 bucket :-  ')
        s3_name=input('Enter S3 Bucket name :-  ')
        o=sp.getstatusoutput('aws s3 cp /root/{} s3://{} --acl public-read'.format(object_name , s3_name))
        print(o[1])
	#removing  Object from S3 bucket:aws
    elif ('remove' in p) and ('object' in p) and ('s3' in p):
        object_name=input('Enter S3 bucket name :-  ')
        s3_name=input('Enter object name :-  ')
        o=sp.getstatusoutput('aws s3 rm s3://{}/{}'.format(object_name , s3_name))
        print(o[1])
	#deleting s3 bucket:aws
    elif ('delete'in p)and ('s3' in p)and('bucket'in p):
        s3_name=input('Enter S3 Bucket name :-  ')
        o=sp.getstatusoutput('aws s3api delete-bucket --bucket {} --region ap-south-1'.format(s3_name))
        print(o[1])
	#create cloudfront with s3:aws
    elif ('create' in p) and('cloudfront' in p ):
        s3_name=input('Enter S3 bucket name :-  ')
        o=sp.getstatusoutput('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(s3_name))
        print(o[1])
	#deleting a  Key Pair:aws
    elif ('delete' in p) or ('remove' in p) and ('key' in p):
        key_name=input('Enter key name to delete :-  ')
        o=sp.getstatusoutput('aws ec2 delete-key-pair --key-name {}'.format(key_name))
        print(o[1])
	#Stoping EC2-Instances:aws
    elif ('stop' in p) and ('ec2' in p)or ('instance' in p):
        ids=input('Enter Instance id to stop Ec2 instances :-  ')
        o=sp.getstatusoutput('aws ec2 stop-instances --instance-ids {}'.format(ids))
        print(o[1])
	#Starting Ec2-Instances:aws
    elif('start'in p) and ('ec2' in p)or ('instance' in p):
        ids=input('Enter Instance id to start Ec2 instances :-  ')
        o=sp.getstatusoutput('aws ec2 start-instances --instance-ids {}'.format(ids))
        print(o[1])
	#terminating  Ec2-Instances:aws
    elif('terminate'in p) and ('ec2' in p)or ('instance' in p):
        ids=input('Enter Instance id to terminate Ec2 instances :-  ')
        o=sp.getstatusoutput('aws ec2 terminate-instances --instance-ids {}'.format(ids))
        print(o[1])
	#deleting security group
    elif('delete' in p) and ('security group' in p):
        o=sp.getstatusoutput('aws ec2 delete-security-group --group-id {}'.format(sg_id))
        print(o[1])
    elif('status' in p) and ('program' in p):
        program=input('Enter your program name to know status :-  ')
        o=sp.getstatusoutput('systemctl status {}'.format(program))
        print(o[1])
    elif('start' in p) and ('program' in p):
        program=input('Enter your program name to start :-  ')
        o=sp.getstatusoutput('systemctl start {}'.format(program))
        print(o[1])
    elif('stop' in p) and ('program' in p):
        program=input('Enter your program name to stop :-  ')
        o=sp.getstatusoutput('systemctl stop {}'.format(program))
        print(o[1])
    elif('install' in p) and ('program' in p):
        program=input('Enter your program name to be install/download :-  ')
        o=sp.getstatusoutput('yum install {}'.format(program))
        print(o[1])
    elif('remove' in p) or ('uninstall' in p) and ('program' in p):
        program=input('Enter your program name to be uninstall/remove :-  ')
        o=sp.getstatusoutput('yum remove {}'.format(program))
        print(o[1])
    elif('docker' in p) and ('images' in p):
        o=sp.getstatusoutput('docker images')
        print(o[1])
    elif('docker' in p) and ('all' in p) and('os' in p):
        o=sp.getstatusoutput('docker ps -a')
        print(o[1])
    elif('docker' in p) and ('running' in p) and('os' in p):
        o=sp.getstatusoutput('docker ps')
        print(o[1])   
    elif('docker' in p) and ('download' in p) and('os' in p):
        os_name=input('Enter your os name to be download :-  ')
        os_version= 'latest'
        os_version=input('Enter your os version :-  ')
        o=sp.getstatusoutput('docker pull {}:{}'.format(os_name,os_version))
        print(o[1])
    elif('docker' in p) and ('run' in p) and('new' in p):
        os_name=input('Enter your  new os name :-  ')
        os_version= 'latest'
        os_version=input('Enter your os version (if specified otherwise press enter):-  ')
        o=sp.getstatusoutput('docker run -it {}:{}'.format(os_name,os_version))
        print(o[1])
    elif('docker' in p) and ('run' in p) and('new' in p):
        os_name=input('Enter your stopped os name/id  :-  ')
        o=sp.getstatusoutput('docker run {}'.format(os_name))
        l=sp.getstatusoutput('docker attach {}'.format(os_name))
        print(l[1])	
    elif('docker' in p) and ('delete' in p) or ('remove' in p):
        os_name=input('Enter your os name/id to remove  :-  ')
        o=sp.getstatusoutput('docker rm {}'.format(os_name))
        print(o[1])
    else:
        print("Sorry, we are updating us to support the same.")
        pyttsx3.speak("Sorry, we are updating us to support the same.")    
