      import os
      import pyttsx3
      import wikipedia
      import datetime
      import time
      import webbrowser
      from datetime import date
      import speech_recognition as sr
      #pyttsx3.speak("Welcome to my text  based chatbot named Dora")
      pyttsx3.speak("Tell me your requirments:")
      while True:     
          r = sr.Recognizer() 
          with sr.Microphone() as source:
              r.energy_threshold = 4000
              r.adjust_for_ambient_noise(source, duration = 3)
              print('we are listening...')
              audio=r.listen(source)
              print('speech done...')

          try:
              #pyttsx3.speak("You said " + r.recognize_google(audio))
              p = r.recognize_google(audio)
          except sr.UnknownValueError:
                  pyttsx3.speak('Sorry, I did not get that')
                  continue

          except sr.RequestError.with_traceback:
                  pyttsx3.speak('Sorry, my service is down')
                  
          q=(('run' in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ('connect' in p))
      
          if (('do not' in p )or ('do nothing' in p) or ("don't" in p) or ('never' in p)):
              pyttsx3.speak('ok as your wish')
              print('ok as your wish')
              continue
            
          #hadoop configuration
          #name node configuration
          elif ("hadoop" in p) and (("configure" in p) or q) and (("master" in p) or ("name" in p)):
              pyttsx3.speak('configuring master node')
              os.system('''cd /etc/hadoop;mkdir /nn;echo "<?xml version="1.0"?>
              <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

              <!-- Put site-specific property overrides in this file. -->

              <configuration>
              <property>
              <name>fs.default.name</name>
              <value>hdfs://0.0.0.0:9001</value>
              </property>
              </configuration>" > core-site.xml; echo "<?xml version="1.0"?>
              <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

              <!-- Put site-specific property overrides in this file. -->

              <configuration>
              <property>
              <name>dfs.name.dir</name>
              <value>/nn</value>
              </property>
              </configuration>" > hdfs-site.xml''')
              pyttsx3.speak('configuration completed')
              break
          #data node configuration
          elif ("hadoop" in p) and (("configure" in p) or q) and (("slave" in p) or ("data" in p)):
              pyttsx3.speak('configuring master node')
              os.system('''cd /etc/hadoop;mkdir /dn;echo "<?xml version="1.0"?>
              <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

              <!-- Put site-specific property overrides in this file. -->

              <configuration>
              <property>
              <name>fs.default.data</name>
              <value>hdfs://0.0.0.0:9001</value>
              </property>
              </configuration>" > core-site.xml; echo "<?xml version="1.0"?>
              <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

              <!-- Put site-specific property overrides in this file. -->

              <configuration>
              <property>
              <name>dfs.data.dir</name>
              <value>/dn</value>
              </property>
              </configuration>" > hdfs-site.xml''')
              pyttsx3.speak('configuration completed')
              break
                  
          #starting namenode   
          elif ("hadoop" in p) and ("start" in p) and (("master" in p) or ("name" in p)):
              pyttsx3.speak("starting namenode")
              os.system("hadoop-daemon.sh start namenode")
              pyttsx3.speak("namenode has started")
            
          #starting datanode       
          elif ("hadoop" in p) and ("start" in p) and (("slave" in p) or ("data" in p)):
              pyttsx3.speak("starting namenode")
              os.system("hadoop-daemon.sh start namenode")
              pyttsx3.speak("datanode has started")
            
          elif ("exit" in p) or ("quit" in p) or ("terminate" in p) or ("end" in p):
              print("Thanks, see yoy again.")
              pyttsx3.speak("Thanks, see yoy again.")
              break
