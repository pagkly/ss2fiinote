global posx, posy, is_recording, autom, pat
        global rec1, snaps, alt, alttext, altpicture, alttext1, rec
        global textclick, root, active, is_playing
        global clickStartX, clickStartY, clickStopX, clickStopY
        global TT
        global snapmode
        global w, h, is_recording, Click, posx, Rightmost, autom

        global pause
        
        
        X, Y=event.Position
        pat = re.compile('Acrobat|Word|SumatraPDF|chrome|opera')
        
#newhndl = ctypes.windll.user32.GetForegroundWindow()
            #focprocess=get_app_name(newhndl)
            #print(focprocess)
            foctitle=win32gui.GetWindowText (win32gui.GetForegroundWindow())
            #print(foctitle)
            #Hold=0
            clickStartXa, clickStartYa=event.Position
            if pause==0 :
                #print("pause not")
                #if Click==1 and clickStartXa<=Rightmost:
                if "tk" in foctitle:
                    pass
                if Click==1 and "tk" not in foctitle:
                    #print("C1")
                    if (snapmode==1):
                        print("snap1")
                        #foctitle=getwintitle2()
                        if (textclick==0):
                            print("t0")
                            TT.config(text="1")
                            clickStartX, clickStartY=event.Position
                            print(clickStartX, clickStartY)
                            if (is_recording==1):
                                print("ir1")
                                TT.config(text="C")
                            textclick=1
                        elif (textclick==1):
                            print("tc1")
                            clickStopX, clickStopY=event.Position
                            print(clickStopX, clickStopY)
                            TT.config(text="2")
                            if (is_playing==1):
                                print("ip1")
                                start_time = time.time()
                            if (active==1):
                                print("act1")
                                if clickStartX>clickStopX :
                                    print("rep")
                                    TT.config(text="Rep")
                                elif (clickStartX<clickStopX) :
                                    print("tried")
                                    import pyscreenshot
                                    clickStartX=int(clickStartX)
                                    clickStartY=int(clickStartY)
                                    clickStopX=int(clickStopX)
                                    clickStopY=int(clickStopY)
                                    im=pyscreenshot.grab(bbox=(clickStartX,clickStartY,clickStopX,clickStopY),childprocess=False)
                                    #C:\\Users\\SP3\\Documents
                                    im.save(dir_path+'\\test.png')
                                    #subprocess.call("xclip -selection clipboard -t image/png -i /root/test.png", shell=True)
                                    TT.config(text="printed")
                            if (is_playing==1):
                                ClipChange()

                            if (is_recording==1):
                                import pyscreenshot
                                global newdir1, objno2
                                TT.config(text="P")
                                if clickStartX<clickStopX :
                                    clickStartX=int(clickStartX)
                                    clickStartY=int(clickStartY)
                                    clickStopX=int(clickStopX)
                                    clickStopY=int(clickStopY)
                                    from time import gmtime,strftime
                                    Time=strftime("%Y%m%d%H%M%S")
                                    picname=Time+'abcdefghijklmno.jpg'
                                    im=pyscreenshot.grab(bbox=(clickStartX,clickStartY,clickStopX,clickStopY),childprocess=False)
                                    #C:\\Users\\SP3\\Documents\\

                                    filename="images.txt"
                                    if os.path.exists(filename):
                                        read2()
                                        pass
                                    else:
                                        newdir1="AOWNLPC00000"+Time
                                        objno2=1
                                        #picdir="AOWNLPC"+Time

                                        import errno
                                        try:
                                            #os.makedirs("C:\\Users\\SP3\\Documents\\images.txt")
                                            #os.makedirs(fnnotespdir+newdir1+".notz")
                                            os.makedirs(fnnotespdir+newdir1+".notz\\attach")
                                            pass
                                        except OSError as e:
                                            if e.errno != errno.EEXIST:
                                                raise
                                        
                                        f1=open(filename,"w+")
                                        f1.write(newdir1+".notz"+'\n'+'Start1')
                                        f1.close()
                                        #f2=open("/media/Surface2/Tech/Automate/FiiNote/Save/@pagkly/notes/"+newdir1+".notz/"+newdir1+"before.note","w+")
                                        #f2.close()

                                    #fnnotespdir+                          
                                    im.save(fnnotespdir+newdir1+'.notz\\attach\\'+picname)
                                    w,h=im.size
                                    print("w="+str(w))
                                    print("h="+str(h))
                                    

                                    newlinehex="0AC480C391C391C39101";
                                    secondobjhex="C88A";
                                    xlochex="E5A5AAE5AB81E5A5A9E19E81E5A5A9E19E81";
                                    posyhex="";
                                    if (objno2<32):
                                        prefixposyhex="A9"
                                        quot=objno2/2;
                                        rem=objno2%2;
                                        objnonow=224+quot+1;

                                    elif (objno2>=32):
                                        prefixposy=int(objno2/34)+169
                                        prefixposyhex=format(math.trunc(prefixposy), 'x')
                                        quot=objno2/2;
                                        rem=objno2%2;
                                        objnonow=224+quot+1;
                                    import math
                                    objnohex=format(math.trunc(objnonow), 'x')
                                    if (quot==0):
                                        if (rem>0):
                                            posyhex="9E"
                                            
                                        else:
                                            posyhex="81"
                                    else:
                                        if (rem!=0):
                                            posyhex="9E"
                                            
                                        elif(rem==0):
                                            posyhex="81"

                                    ylochex="E5A5A9E19E81E5A5AAE5AB81E5A5"+prefixposyhex+objnohex+posyhex+"81"
                                    zlochex="E5A5A9E19E81E5A5A9E19E81E5A5AAE5AB81"
                                    if (w<128):
                                        xpixshex=format(w,'x')
                                        xpixshex=str(xpixshex).zfill(2)
                                        
                                    if (w>=128):
                                        xquothexint=int(math.trunc(192+(w/64)));
                                        xremhexint=int(math.trunc(128+(w%64)));
                                        xquothexs=format(xquothexint,'x')
                                        xremhexs=format(xremhexint,'x')
                                        xpixshex=xquothexs+xremhexs;


                                    if (h<128):
                                        ypixshex=format(h,'x')
                                        ypixshex=str(ypixshex).zfill(2)
                                        
                                    if (h>=128):
                                        yquothexint=int(math.trunc(192+(h/64)));
                                        yremhexint=int(math.trunc(128+(h%64)));

                                        yquothexs=format(yquothexint,'x')
                                        yremhexs=format(yremhexint,'x')
                                    
                                        ypixshex=yquothexs+yremhexs;

                                    yscalehexs="";
                                    xscalehexs="";
                                    ysuffix="";

                                    if (w<h):
                                        a=2717*w;
                                        div=h*64;
                                        xscalequotinta=int(math.trunc(a/div));
                                        xscalequotint=148+xscalequotinta;

                                        xscalequothexs=format(xscalequotint,'x')
                                        xrem=(((a/div)-xscalequotinta)*64);
                                        xscaleremint=int(128+xrem);
                                        
                                        xscaleremhexs=format(xscaleremint,'x')
                                        xscalehexs="E2"+xscalequothexs+xscaleremhexs;
                                        yscalehexs="E2BE9D";
                                    elif (w>h):
                                        xscalehexs="E38EBF";
                                        a=3711*h;
                                        div=w*64;
                                        yscalequotint=0;
                                        yscalequotinta=int(math.trunc(a/div));

                                        if (yscalequotinta>=43):
                                            ysuffix="E3";
                                            yscalequotint=int(math.trunc(128+(((3711*h)/(w*64))-43)));

                                        elif (yscalequotinta<43):
                                            ysuffix="E2";
                                            yscalequotint=int(math.trunc(148+((3711*h)/(w*64))));
                                        yscalequothexs=format(yscalequotint,'x')
                                        yrem=int(math.trunc((((a/div)-yscalequotinta)*64)));
                                        yscaleremint=int(128+yrem);
                                        yscaleremhexs=format(yscaleremint,'x')
                                        yscalehexs=ysuffix+yscalequothexs+yscaleremhexs;
                                    elif (w==h):
                                        xscalehexs="E2BAA3";
                                        yscalehexs="E2BAA3";
                                    else:
                                        xscalehexs="E2BAA3";
                                        yscalehexs="E2BAA3";



                                    objscalehex="0303E293B903E293B903"+xscalehexs+"03"+yscalehexs+"22";

                                    import binascii
                                    picnamehex="".join("{:02x}".format(ord(c)) for c in picname)
                                    
                                    hexc = newlinehex+secondobjhex+xlochex+ylochex+zlochex+objscalehex+picnamehex+xpixshex+ypixshex+"01";
                                    #print(hexc)
                                    
                                    
                                    f3=fnnotespdir+newdir1+".notz\\"+newdir1+".note"
                                    if os.path.exists(f3):
                                        with open(f3,"rb") as f:
                                            content=f.read()
                                            contenthex=str(binascii.hexlify(content).decode('utf-8'))
                                        append=contenthex+hexc
                                        
                                    elif not os.path.exists(f3):
                                        contenthex=""
                                        append=contenthex+hexc
                                            
                                    print(len(append))
                                    with open(f3,"wb") as fout:
                                        append=bytes(bytearray.fromhex(append))
                                        fout.write(append)
                                        
                                    
                                    objno2+=1
                                    os.remove(filename)
                                    f1=open(filename,"w+")
                                    f1.write(newdir1+".notz"+'\n'+'Start'+str(objno2))
                                    f1.close()

                                    if (objno2>=30):
                                        callbackp()
                                        Suspend()
                                        TT.config(text="New Folder")
                                    else:
                                        TT.config(text="appended")
                                    
                                elif clickStartX<clickStopX:
                                    TT.config(text="Rep")
                                else:
                                    TT.config(text="Rep")
                            textclick=0
                            
                    #if snapmode==0 and pause==0 and is_recording==0 and "None" not in str(pat.search(str(focprocess))):
                    if snapmode==0 and pause==0 and is_recording==0 :
                        Default()
                        picdown=1
                        autom=5
                        active=0
                        #foctitle=getwintitle()
                        #focprocess=subprocess.getoutput("xprop -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d ' ' -f 5) WM_CLASS | cut -d= -f 2 | tr -d '\"' ")
                        if "SumatraPDF" in str(foctitle):
                            pass
                        textclick=0
                        is_recording = 1
                        pause=0
                        snapmode=1
                        TT.config(text="Recording")
                        print("rec")
                        return True
            return True

